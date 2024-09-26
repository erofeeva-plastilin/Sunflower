# Sunflower
**Путь ко всем файлам: ```/mnt/users/erofeevan/Prediction/```** 
Структура папки Data:        
Data/      
├── Genotype/ #тут обработанные vcf файлы после скрипта pos.py      
│       ├── Categorical/ #обработанные vcf файлы после скрипта pos.py для категориальных/бинарных фенотипов      
│       ├── Quantitative/ #обработанные vcf файлы после скрипта pos.py для непрерывных фенотипов      
├── Phenotype/ #тут обработанные данные с тестируемыми аллелями и эффектом      
        ├── Categorical_phenotype/ #категориальные/бинарные фенотипы         
        ├── Quantitative_phenotype/ #непрерывные фенотипы      
Некоторые фенотипы имеют суффикс "one" - фенотип из статьи https://www.mdpi.com/2073-4425/15/7/950, "two" - фенотип из статьи https://www.nature.com/articles/s41586-020-2467-6#MOESM3
В папке Results результаты предсказаний      
В папке Scripts два необходимых скрипта         
## Создание output файлов
Фильтрация нужных SNP:
```
python3 pos.py -p {input positions} -i {input.vcf} -o {output_vcf.tsv}
```
**Пример запуска**
```
python3 pos.py -p CMS.txt -i 2024-08-30_wgs_sunflower.vcf -o CMS_vcf.tsv
```
Результаты этой фильтрации в:
Data/      
├── Genotype/ #тут обработанные vcf файлы после скрипта pos.py      
│       ├── Categorical/ #обработанные vcf файлы после скрипта pos.py для категориальных/бинарных фенотипов      
│       ├── Quantitative/ #обработанные vcf файлы после скрипта pos.py для непрерывных фенотипов   
## Предсказание фенотипов 
```
python script_name.py --plink_table {input_pheno.tsv} --vcf {input_vcf.tsv} --output {output} --ld 100000 --max_phenotype 1 --min_phenotype 0 --het
```
**Пример запуска**
```
python3 prediction.py --plink_table CMS_pheno.tsv  --vcf CMS_vcf.tsv --output CMS.tsv --ld 100000 --max_phenotype 1 --min_phenotype 0 --het
```
input_pheno.tsv - файл из папки Phenotype   
input_vcf.tsv - файл из папки Genotype   
output - название фенотипа
Результат скрипта в папке Results    
Итоговые результаты по ссылке: https://docs.google.com/spreadsheets/d/1EardKid4snJ8-MThG1VvoeIXrowbNzZy6gZeXXGWahM/edit?gid=0#gid=0
