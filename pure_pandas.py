import helper
import pandas as pd
import configparser

connection = helper.get_connection()
CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

query = '''
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

df = pd.read_sql_query(query,connection)
df.to_csv(CONFIG['SQLITE_CONFIG']['df_csv_filename'], sep=';', index=False)
# import numpy as np
# np.savetxt(CONFIG['SQLITE_CONFIG']['df_csv_filename'], df, delimiter=';')


# cursor = cursor.execute(query)
# columns = list(map(lambda x: x[0], cursor.description))
# rows = cursor.fetchall()

# helper.generate_csv(columns, rows)

# cursor.close()
