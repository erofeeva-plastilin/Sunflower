import pandas as pd
import numpy as np
import argparse

# Функция для чтения позиций и подготовки данных
def datasets_preparing(plink_output, vcf, ld):
    vcf["SNP"] = vcf["#CHROM"].astype(str) + ":" + vcf["POS"].astype(str)
    plink_output["SNP"] = plink_output["#CHROM"].astype(str) + ":" + plink_output["POS"].astype(str)
    plink_output[f'POS_{ld}'] = plink_output.POS // ld
    plink_output_uniq = plink_output.groupby(['#CHROM', f'POS_{ld}'],group_keys=False)\
                                    .apply(lambda x: x.sort_values(['BETA'], ascending=False)\
                                    .head(1))
    plink_output_uniq['REF_eff'] = np.nan
    plink_output_uniq['ALT_eff'] = np.nan
    plink_output_uniq['REF_eff'] = plink_output_uniq['REF_eff']\
                                    .mask(plink_output_uniq.REF == plink_output_uniq.A1, plink_output_uniq.BETA)\
                                    .fillna(0)
    plink_output_uniq['ALT_eff'] = plink_output_uniq['ALT_eff']\
                                    .mask(plink_output_uniq.ALT == plink_output_uniq.A1, plink_output_uniq.BETA)\
                                    .fillna(0)
    return plink_output_uniq, vcf
# Функция для обработки генотипов
def process_genotype(genotype, ref_effect, alt_effect, het):
    if genotype == '0/0':
        return ref_effect
    elif genotype == '1/1':
        return alt_effect
    elif genotype == './.':
        return 0
    elif '0/1' in genotype:
        return max(ref_effect, alt_effect) / 2 if het else 0
    elif '0/2' in genotype or '1/2' in genotype:
        return alt_effect 
    else:
        return 0
# Основная функция для расчета предсказанных фенотипов
def calculating_predicted_phenotypes(plink_output, vcf, ld, max_phenotype, min_phenotype, het):
    plink_output_uniq, vcf_edited = datasets_preparing(plink_output, vcf, ld)
    markers_effect = plink_output_uniq.BETA.sum()
    coef = markers_effect / (max_phenotype - min_phenotype)
    vcf_values = vcf_edited[vcf_edited.SNP.isin(plink_output_uniq.SNP)]
    plink_output_uniq = plink_output_uniq[plink_output_uniq.SNP.isin(vcf_edited.SNP)]
    for i in range(vcf_values.shape[0]):
        snp_id = vcf_values.iloc[i, vcf_values.columns.get_loc('SNP')]
        ref_effect = float(plink_output_uniq[plink_output_uniq.SNP == snp_id].REF_eff)
        alt_effect = float(plink_output_uniq[plink_output_uniq.SNP == snp_id].ALT_eff)
        for j in range(2, vcf_values.shape[1]): 
            genotype = vcf_values.iloc[i, j]
            vcf_values.iloc[i, j] = process_genotype(genotype, ref_effect, alt_effect, het)
    vcf_values = vcf_values.set_index("SNP")
    vcf_values = vcf_values.drop(["#CHROM", "POS"], axis=1)
    vcf_values_protein = vcf_values / coef
    predicted_rank = vcf_values.sum()
    predicted_rank.name = "predicted_rank"
    predicted_protein = vcf_values_protein.sum() + min_phenotype
    predicted_protein.name = "predicted_protein"
    summary_samples = pd.concat([predicted_rank, predicted_protein], axis=1)
    return vcf_values, vcf_values_protein, summary_samples
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Расчет предсказанных фенотипов на основе PLINK и VCF данных")
    parser.add_argument('--plink_table', type=str, required=True, help='Путь к файлу PLINK с фенотипическими данными')
    parser.add_argument('--vcf', type=str, required=True, help='Путь к файлу VCF')
    parser.add_argument('--output', type=str, required=True, help='Префикс для выходного файла')
    parser.add_argument('--ld', type=int, default=100000, help='Генетическое расстояние в bp для группировки маркеров')
    parser.add_argument('--max_phenotype', type=float, default=1.0, help='Максимальное значение фенотипа')
    parser.add_argument('--min_phenotype', type=float, default=0.0, help='Минимальное значение фенотипа')
    parser.add_argument('--het', action='store_true', help='Считать гетерозиготы как половину значения эффекта (если указан)')
    args = parser.parse_args()
    # Чтение файлов
    vcf_file = pd.read_csv(args.vcf, sep='\t')
    plink_file = pd.read_csv(args.plink_table, sep='\t')
    # Вычисление предсказанных фенотипов
    vcf_values, vcf_values_protein, summary_samples = calculating_predicted_phenotypes(
        plink_file, vcf_file, ld=args.ld, max_phenotype=args.max_phenotype, min_phenotype=args.min_phenotype, het=args.het
    )
    # Сохранение результата
    summary_samples.to_csv(f"{args.output}_samples_summary.tsv", sep='\t')
