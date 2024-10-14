# Sunflower
**Путь ко всем файлам: ```/mnt/users/erofeevan/Prediction/```**     
В папке Scripts три необходимых скрипта         
## Создание output файлов
Фильтрация нужных SNP:
```
python3 pos.py -p {input positions} -i {input.vcf} -o {output_vcf.tsv}
```
**Пример запуска**
```
python3 pos.py -p CMS.txt -i 2024-08-30_wgs_sunflower.vcf -o CMS_vcf.tsv
```  
## Предсказание фенотипов 
```
python script_name.py --plink_table {input_pheno.tsv} --vcf {input_vcf.tsv} --output {output} --ld 100000 --max_phenotype 1 --min_phenotype 0 --het
```
Для категориальных фенотипов -max_phenotype 1 --min_phenotype 0, для непрерывных определяется согласно результатам фенотипирования   
**Пример запуска**
```
python3 prediction.py --plink_table CMS_pheno.tsv  --vcf CMS_vcf.tsv --output CMS.tsv --ld 100000 --max_phenotype 1 --min_phenotype 0 --het
```
Итоговые результаты по ссылке: https://docs.google.com/spreadsheets/d/1EardKid4snJ8-MThG1VvoeIXrowbNzZy6gZeXXGWahM/edit?gid=0#gid=0

```
python3 pos.py -p FT_pos.txt -i 14102024Sun_tabs.vcf -o FT_vcf.tsv
python3 pos.py -p PH_pos.txt -i 14102024Sun_tabs.vcf -o PH_vcf.tsv
python3 pos.py -p SD_pos.txt -i 14102024Sun_tabs.vcf -o SD_vcf.tsv
python3 pos.py -p SW_pos.txt -i 14102024Sun_tabs.vcf -o SW_vcf.tsv
python3 pos.py -p KW_pos.txt -i 14102024Sun_tabs.vcf -o KW_vcf.tsv

python3 pos.py -p Days_to_budding_pos.txt -i 14102024Sun_tabs.vcf -o Days_to_budding_vcf.tsv
python3 pos.py -p Days_To_Flowering_pos.txt -i 14102024Sun_tabs.vcf -o Days_To_Flowering_vcf.tsv
python3 pos.py -p Internode_length_pos.txt -i 14102024Sun_tabs.vcf -o Internode_length_vcf.tsv
python3 pos.py -p Leaf_curvedHeight_maxWidth_pos.txt -i 14102024Sun_tabs.vcf -o Leaf_curvedHeight_maxWidth_vcf.tsv
python3 pos.py -p LIR_pos.txt -i 14102024Sun_tabs.vcf -o LIR_vcf.tsv
python3 pos.py -p Leaf_shape_index_external_I_pos.txt -i 14102024Sun_tabs.vcf -o Leaf_shape_index_external_I_vcf.tsv
python3 pos.py -p Leaf_shape_index_external_II_pos.txt -i 14102024Sun_tabs.vcf -o Leaf_shape_index_external_II_vcf.tsv
python3 pos.py -p Leaf_total_C_pos.txt -i 14102024Sun_tabs.vcf -o Leaf_total_C_vcf.tsv
python3 pos.py -p Petiole_main_veins_colour_pos.txt -i 14102024Sun_tabs.vcf -o Petiole_main_veins_colour_vcf.tsv
python3 pos.py -p Plant_height_at_flowering_pos.txt -i 14102024Sun_tabs.vcf -o Plant_height_at_flowering_vcf.tsv
python3 pos.py -p Primary_branches_pos.txt -i 14102024Sun_tabs.vcf -o Primary_branches_vcf.tsv
python3 pos.py -p Seed_proximal_eccentricity_pos.txt -i 14102024Sun_tabs.vcf -o Seed_proximal_eccentricity_vcf.tsv
python3 pos.py -p TLN_pos.txt -i 14102024Sun_tabs.vcf -o TLN_vcf.tsv
python3 pos.py -p Trichomes_density_edge_average_pos.txt -i 14102024Sun_tabs.vcf -o Trichomes_density_edge_average_vcf.tsv
python3 pos.py -p Trichomes_density_leaf_edge_flat_area_pos.txt -i 14102024Sun_tabs.vcf -o Trichomes_density_leaf_edge_flat_area_vcf.tsv
python3 pos.py -p Trichomes_density_leaf_edge_secondary_veins_pos.txt -i 14102024Sun_tabs.vcf -o Trichomes_density_leaf_edge_secondary_veins_vcf.tsv
```
```
python3 prediction.py --plink_table KW_pheno.tsv  --vcf KW_vcf.tsv --output KW --ld 100000 --max_phenotype 8.83 --min_phenotype 1.02 --het
python3 prediction.py --plink_table SW_pheno.tsv  --vcf SW_vcf.tsv --output SW --ld 100000 --max_phenotype 14.81 --min_phenotype 1.25 --het
python3 prediction.py --plink_table FT_pheno.tsv  --vcf FT_vcf.tsv --output FT --ld 100000 --max_phenotype 91.7 --min_phenotype 55.7 --het
python3 prediction.py --plink_table SD_pheno.tsv  --vcf SD_vcf.tsv --output SD --ld 100000 --max_phenotype 31.7 --min_phenotype 10.9 --het
python3 prediction.py --plink_table PH_pheno.tsv  --vcf PH_vcf.tsv --output PH --ld 100000 --max_phenotype 281.7 --min_phenotype 88.8 --het

python3 prediction.py --plink_table Days_to_budding_pheno.tsv  --vcf Days_to_budding_vcf.tsv  --output Days_to_budding --ld 100000  --max_phenotype 107 --min_phenotype 8 --het
python3 prediction.py --plink_table Days_To_Flowering_pheno.tsv  --vcf Days_To_Flowering_vcf.tsv  --output Days_To_Flowering --ld 100000  --max_phenotype 131 --min_phenotype 30 --het
python3 prediction.py --plink_table Internode_length_pheno.tsv  --vcf Internode_length_vcf.tsv  --output Internode_length --ld 100000  --max_phenotype 11.1285714 --min_phenotype 1.63461538 --het
python3 prediction.py --plink_table Leaf_curvedHeight_maxWidth_pheno.tsv  --vcf Leaf_curvedHeight_maxWidth_vcf.tsv  --output Leaf_curvedHeight_maxWidth --ld 100000  --max_phenotype 3.00052339 --min_phenotype 1.189239994 --het
python3 prediction.py --plink_table LIR_pheno.tsv  --vcf LIR_vcf.tsv  --output Leaf_Initiation_Rate_(LIR) --ld 100000  --max_phenotype 1.8 --min_phenotype 0.419354839 --het
python3 prediction.py --plink_table Leaf_shape_index_external_I_pheno.tsv  --vcf Leaf_shape_index_external_I_vcf.tsv  --output Leaf_shape_index_external_I --ld 100000  --max_phenotype 2.9882 --min_phenotype 1.0919 --het
python3 prediction.py --plink_table Leaf_shape_index_external_II_pheno.tsv  --vcf Leaf_shape_index_external_II_vcf.tsv  --output Leaf_shape_index_external_II --ld 100000  --max_phenotype 3.9412 --min_phenotype 1.0711 --het
python3 prediction.py --plink_table Leaf_total_C_pheno.tsv  --vcf Leaf_total_C_vcf.tsv  --output Leaf_total_C --ld 100000  --max_phenotype 57.423 --min_phenotype 28.477 --het
python3 prediction.py --plink_table Petiole_main_veins_colour_pheno.tsv  --vcf Petiole_main_veins_colour_vcf.tsv  --output Petiole_main_veins_colour --ld 100000  --max_phenotype 4 --min_phenotype 0 --het
python3 prediction.py --plink_table Plant_height_at_flowering_pheno.tsv  --vcf Plant_height_at_flowering_vcf.tsv  --output Plant_height_at_flowering --ld 100000  --max_phenotype 422 --min_phenotype 32.8 --het
python3 prediction.py --plink_table Primary_branches_pheno.tsv  --vcf Primary_branches_vcf.tsv  --output Primary_branches --ld 100000  --max_phenotype 85 --min_phenotype 6 --het
python3 prediction.py --plink_table Seed_proximal_eccentricity_pheno.tsv  --vcf Seed_proximal_eccentricity_vcf.tsv  --output Seed_proximal_eccentricity --ld 100000  --max_phenotype 0.8937625 --min_phenotype 0.7964 --het
python3 prediction.py --plink_table TLN_pheno.tsv  --vcf TLN_vcf.tsv  --output Total_leaf_number_(TLN) --ld 100000  --max_phenotype 87 --min_phenotype 8 --het
python3 prediction.py --plink_table Trichomes_density_edge_average_pheno.tsv  --vcf Trichomes_density_edge_average_vcf.tsv  --output Trichomes_density_edge_average --ld 100000  --max_phenotype 227.5 --min_phenotype 12 --het
python3 prediction.py --plink_table Trichomes_density_leaf_edge_flat_area_pheno.tsv  --vcf Trichomes_density_leaf_edge_flat_area_vcf.tsv  --output Trichomes_density_leaf_edge_flat_area --ld 100000  --max_phenotype 297 --min_phenotype 7 --het
python3 prediction.py --plink_table Trichomes_density_leaf_edge_secondary_veins_pheno.tsv  --vcf Trichomes_density_leaf_edge_secondary_veins_vcf.tsv  --output Trichomes_density_leaf_edge_secondary_veins --ld 100000  --max_phenotype 221 --min_phenotype 5 --het
```
