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
