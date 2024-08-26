import pandas as pd

# Создание DataFrame
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'IT'],
    'Salary': [70000, 80000, 75000, 60000, 72000],
    'JoiningDate': ['2020-01-15', '2019-03-12', '2021-07-23', '2018-11-30', '2019-05-19']
}

df = pd.DataFrame(data)
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])
print("DataFrame о сотрудниках:\n", df)

# Вывод первых 3 строк
print("\nПервые 3 строки DataFrame:\n", df.head(3))

# Вывод последних 2 строк
print("\nПоследние 2 строки DataFrame:\n", df.tail(2))


# Сотрудники с зарплатой больше 70,000
high_salary_df = df[df['Salary'] > 70000]
print("\nСотрудники с зарплатой > 70,000:\n", high_salary_df)

# Сотрудники из отдела IT
it_department_df = df[df['Department'] == 'IT']
print("\nСотрудники из отдела IT:\n", it_department_df)


# Средняя зарплата
average_salary = df['Salary'].mean()
print("\nСредняя зарплата сотрудников:\n", average_salary)

# Максимальная зарплата
max_salary = df['Salary'].max()
print("\nМаксимальная зарплата сотрудников:\n", max_salary)


# Сортировка по зарплате в порядке убывания
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nDataFrame отсортированный по зарплате:\n", sorted_df)


# Добавление столбца 'YearsAtCompany'
df['YearsAtCompany'] = (pd.Timestamp.now() - df['JoiningDate']).dt.days // 365
print("\nDataFrame с новым столбцом 'YearsAtCompany':\n", df)


# Изменение зарплаты сотрудника с EmployeeID 104
df.loc[df['EmployeeID'] == 104, 'Salary'] = 62000
print("\nDataFrame после изменения зарплаты:\n", df)
