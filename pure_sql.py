import helper

connection = helper.get_connection()
cursor = connection.cursor()
    

sql = '''
    SELECT
        c.customer_id  as Customer,
        c.age  as Age,
        i.item_name as Item,
        o.quantity  as Quantity
    FROM Customers c 
    INNER JOIN Sales s on c.customer_id  = s.customer_id 
    INNER JOIN Orders o on o.sales_id  = s.sales_id 
    INNER JOIN Items i on i.item_id = o.item_id
'''

cursor = cursor.execute(sql)
columns = list(map(lambda x: x[0], cursor.description))
rows = cursor.fetchall()

helper.generate_csv(columns, rows)
cursor.close()
