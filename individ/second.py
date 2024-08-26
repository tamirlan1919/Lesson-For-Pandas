import pandas as pd

# Данные о студентах
data_students = {
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Jane', 'Alice', 'Bob', 'Charlie'],
    'Course': ['Math', 'Science', 'Math', 'History', 'Science'],
    'Grade': [85, 90, 78, 88, 92]
}

df_students = pd.DataFrame(data_students)
print("DataFrame о студентах:\n", df_students)


# Средняя оценка по каждому курсу
average_grade_by_course = df_students.groupby('Course')['Grade'].mean()
print("\nСредняя оценка по каждому курсу:\n", average_grade_by_course)


# Студент с наивысшим баллом
highest_grade = df_students['Grade'].max()
top_student = df_students[df_students['Grade'] == highest_grade]
print("\nСтудент с наивысшим баллом:\n", top_student)


# Добавление столбца 'Pass/Fail'
df_students['Pass/Fail'] = df_students['Grade'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
print("\nDataFrame с новым столбцом 'Pass/Fail':\n", df_students)


