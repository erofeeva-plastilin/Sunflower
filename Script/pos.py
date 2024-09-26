import argparse
# Функция для чтения позиций
def read_positions(file_path):
    positions = {}
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                chrom, pos = line.strip().split('\t')
                if chrom not in positions:
                    positions[chrom] = set()
                positions[chrom].add(int(pos))
    return positions
# Функция для фильтрации
def filter_vcf(vcf_file_path, output_file_path, positions_file):
    positions = read_positions(positions_file)
    with open(vcf_file_path, "r") as vcf_file, open(output_file_path, "w") as output_file:
        header_found = False
        for line in vcf_file:
            if line.startswith('#'):
                if line.startswith("#CHROM"):
                    # Записываем заголовок, убрав ненужные колонки
                    header_columns = line.strip().split('\t')
                    # Удаляем ненужные колонки в заголовке
                    header_columns = [col for col in header_columns if col not in ['ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']]
                    output_file.write('\t'.join(header_columns) + '\n')
                    header_found = True
                continue
            if header_found:
                columns = line.strip().split('\t')
                chrom = columns[0]
                position = int(columns[1])   
                if chrom in positions and position in positions[chrom]:
                    columns = columns[:2] + columns[9:] 
                    genotype_columns = columns[2:] 
                    genotype_columns = [gt.split(":")[0] for gt in genotype_columns]
                    output_file.write('\t'.join(columns[:2] + genotype_columns) + '\n')
if __name__ == "__main__":
    # Аргумент для указания файла с позициями
    parser = argparse.ArgumentParser(description="Фильтрация VCF по позициям")
    parser.add_argument('-p', '--positions', type=str, required=True, help="Путь к файлу с позициями")
    parser.add_argument('-i', '--input_vcf', type=str, required=True, help="Путь к входному VCF файлу")
    parser.add_argument('-o', '--output', type=str, required=True, help="Путь к выходному файлу")
    args = parser.parse_args()
    filter_vcf(args.input_vcf, args.output, args.positions)
