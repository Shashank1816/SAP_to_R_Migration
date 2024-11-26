import pandas as pd
import mysql.connector
from datetime import datetime

# Connect to MySQL database
# Note: Replace these with your actual database connection details
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

# Clean up: Delete existing tables if they exist
try:
    cursor.execute("DROP TABLE IF EXISTS testblkld1")
    cursor.execute("DROP TABLE IF EXISTS testblkld2")
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Create work data set
data = {
    'name': ['amy', 'bill', 'charlie', 'david', 'elinor', 'pearl', 'vera', 'frank', 'georgia', 'henry', 'joann', 'buddy'],
    'age': [3, 12, 35, 19, 42, 78, 96, 24, 1, 46, 27, 66],
    'sex': ['f', 'm', 'm', 'm', 'f', 'f', 'f', 'm', 'f', 'm', 'f', 'm'],
    'bdate': ['03/01/85', '12/12/77', '01/02/53', '10/14/69', '08/08/45', '05/12/22', '10/12/00', '09/26/63', '04/06/87', '05/30/42', '02/04/61', '10/14/32']
}

df = pd.DataFrame(data)
df['bdate'] = pd.to_datetime(df['bdate'], format='%m/%d/%y')

# Create table in MySQL
create_table_query = """
CREATE TABLE testblkld1 (
    name VARCHAR(255),
    age INT,
    sex CHAR(1),
    bdate DATE
)
"""
cursor.execute(create_table_query)

# Bulk insert data into MySQL
insert_query = "INSERT INTO testblkld1 (name, age, sex, bdate) VALUES (%s, %s, %s, %s)"
values = [(row.name, row.age, row.sex, row.bdate.strftime('%Y-%m-%d')) for row in df.itertuples()]
cursor.executemany(insert_query, values)

conn.commit()
cursor.close()
conn.close()

print("Data has been successfully bulk loaded into the database.")