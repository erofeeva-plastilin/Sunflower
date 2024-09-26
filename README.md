# Sunflower
**Путь ко всем файлам: ```/mnt/users/erofeevan/Prediction/```** 
Структура папки Data:        
Data/      
├── Genotype/ #тут обработанные vcf файлы после скрипта pos.py      
│   ├── Categorical/ #обработанные vcf файлы после скрипта pos.py для категориальных/бинарных фенотипов      
│   ├── Quantitative/ #обработанные vcf файлы после скрипта pos.py для непрерывных фенотипов      
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
# Пример запуска
python3 pos.py -p CMS.txt -i 2024-08-30_wgs_sunflower.vcf -o CMS_vcf.tsv
```
Результаты этой фильтрации в:
Data/      
├── Genotype/ #тут обработанные vcf файлы после скрипта pos.py      
│   ├── Categorical/ #обработанные vcf файлы после скрипта pos.py для категориальных/бинарных фенотипов      
│   ├── Quantitative/ #обработанные vcf файлы после скрипта pos.py для непрерывных фенотипов   
