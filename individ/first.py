import pandas as pd

# Данные о продажах
data_sales = {
    'OrderID': [201, 202, 203, 204, 205],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Mouse'],
    'Quantity': [1, 3, 2, 1, 2],
    'Price': [1200, 25, 75, 300, 25],
    'OrderDate': ['2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14']
}

df_sales = pd.DataFrame(data_sales)
df_sales['OrderDate'] = pd.to_datetime(df_sales['OrderDate'])
print("DataFrame о продажах:\n", df_sales)

# Добавление столбца с общей стоимостью заказа
df_sales['Total'] = df_sales['Quantity'] * df_sales['Price']
total_revenue = df_sales['Total'].sum()
print("\nОбщий доход от продаж:\n", total_revenue)

# Продукт с максимальным количеством
most_sold_product = df_sales[df_sales['Quantity'] == df_sales['Quantity'].max()]
print("\nПродукт, купленный в наибольшем количестве:\n", most_sold_product[['Product', 'Quantity']])


# Фильтрация заказов с количеством больше 1
bulk_orders = df_sales[df_sales['Quantity'] > 1]
print("\nЗаказы, где количество товара больше 1:\n", bulk_orders)

