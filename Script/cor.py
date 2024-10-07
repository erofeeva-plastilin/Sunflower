import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Загрузка данных из файла, где строки содержат образцы, а первый столбец содержит признаки
df = pd.read_csv('/content/df.txt', sep='\t', index_col=0)
# Транспонирование таблицы, чтобы признаки стали столбцами
df = df.transpose()
# Расчет корреляционной матрицы между признаками
correlation_matrix = df.corr()
# Печать корреляционной матрицы
print(correlation_matrix)
# Визуализация корреляционной матрицы
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, xticklabels=correlation_matrix.columns, yticklabels=correlation_matrix.columns)
plt.title('Correlation Matrix between Features')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
