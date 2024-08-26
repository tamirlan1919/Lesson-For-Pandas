import pandas as pd

# Данные о температуре
data_temp = {
    'Date': ['2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05', '2024-08-06', '2024-08-07'],
    'Temperature': [23.5, 24.0, 22.8, 23.0, 24.2, 25.1, 24.8]
}

df_temp = pd.DataFrame(data_temp)
df_temp['Date'] = pd.to_datetime(df_temp['Date'])
print("DataFrame о температуре:\n", df_temp)


# Средняя температура
average_temp = df_temp['Temperature'].mean()
print("\nСредняя температура за неделю:\n", average_temp)


# Максимальная температура
max_temp = df_temp['Temperature'].max()
print("\nМаксимальная температура:\n", max_temp)

# Минимальная температура
min_temp = df_temp['Temperature'].min()
print("\nМинимальная температура:\n", min_temp)


# Добавление столбца 'AboveAverage'
df_temp['AboveAverage'] = df_temp['Temperature'] > average_temp
print("\nDataFrame с новым столбцом 'AboveAverage':\n", df_temp)
