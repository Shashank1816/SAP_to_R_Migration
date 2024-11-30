```python
import pandas as pd
import numpy as np
import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# =========================
# LIBNAME Sample 1
# =========================
df_samdat7 = pd.read_sql_query("SELECT lname, fname, state, hphone FROM SAMDAT7 WHERE state = 'NJ'", conn)
print("Libname Sample 1: New Jersey Phone List")
print(df_samdat7)

# =========================
# LIBNAME Sample 2
# =========================
df_samdat5 = pd.read_sql_query("SELECT * FROM SAMDAT5", conn)
df_highwage = df_samdat5.drop(columns=['sex', 'birth', 'hired'])
df_highwage['CATEGORY'] = np.where(df_highwage['salary'] > 60000, 'High',
                                    np.where(df_highwage['salary'] < 30000, 'Low', 'Avg'))
print("Libname Sample 2: Salary Analysis")
print(df_highwage[['salary', 'CATEGORY']].style.format({'salary': "${:,.2f}".format}))

# =========================
# LIBNAME Sample 3
# =========================
df_samdat8 = pd.read_sql_query("SELECT * FROM SAMDAT8", conn)
df_combined = pd.merge(df_samdat7, df_samdat8.rename(columns={'SUPID': 'IDNUM'}), on='IDNUM', how='inner')
print("Libname Sample 3: Supervisor Information")
print(df_combined)

# =========================
# LIBNAME Sample 4
# =========================
df_samdat6 = pd.read_sql_query("SELECT * FROM SAMDAT6", conn)
df_payroll = pd.concat([df_samdat5, df_samdat6]).drop_duplicates(subset='IDNUM', keep='last')
print("Libname Sample 4: Updated Payroll Data")
print(df_payroll)

# =========================
# LIBNAME Sample 5
# =========================
df_total_salary = df_samdat5.groupby('JOBCODE').agg(total=('SALARY', 'sum')).reset_index()
df_total_salary['total'] = df_total_salary['total'].apply(lambda x: "${:,.2f}".format(x))
print("Libname Sample 5: Total Salary by Jobcode")
print(df_total_salary)

# =========================
# LIBNAME Sample 6
# =========================
df_flights = pd.read_sql_query("SELECT DATES, DEST FROM SAMDAT2 WHERE DEST IN ('FRA', 'LON') ORDER BY DEST", conn)
print("Libname Sample 6: Flights to London and Frankfurt")
print(df_flights)

# =========================
# LIBNAME Sample 7
# =========================
df_international_flights = pd.read_sql_query("SELECT FLIGHT, DATES, DEST, BOARDED FROM SAMDAT3 WHERE BOARDED > 200 ORDER BY FLIGHT", conn)
print("Libname Sample 7: International Flights by Flight Number with Over 200 Passengers")
print(df_international_flights)

# =========================
# LIBNAME Sample 8
# =========================
df_employees = pd.read_sql_query("SELECT a.LNAME, a.FNAME, b.SALARY FROM SAMDAT7 a JOIN SAMDAT5 b ON a.IDNUM = b.IDNUM WHERE b.SALARY > 40000", conn)
df_employees['SALARY'] = df_employees['SALARY'].apply(lambda x: "${:,.2f}".format(x))
print("Libname Sample 8: Employees with salary greater than $40,000")
print(df_employees)

# =========================
# LIBNAME Sample 9a
# =========================
df_delayed_flights_a = pd.read_sql_query("""
SELECT DISTINCT samdat1.FLIGHT, samdat1.DATES, DELAY 
FROM SAMDAT1 
JOIN SAMDAT2 ON samdat1.FLIGHT = samdat2.FLIGHT AND samdat1.DATES = samdat2.DATES 
JOIN SAMDAT3 ON samdat1.FLIGHT = samdat3.FLIGHT 
WHERE DELAY > 0 
ORDER BY DELAY DESC
""", conn)
print("Libname Sample 9a: Delayed International Flights in March")
print(df_delayed_flights_a)

# =========================
# LIBNAME Sample 9b
# =========================
df_delayed_flights_b = pd.read_sql_query("""
SELECT DISTINCT samdat1.FLIGHT, samdat1.DATES, DELAY 
FROM SAMDAT1 
JOIN SAMDAT2 ON samdat1.FLIGHT = samdat2.FLIGHT AND samdat1.DATES = samdat2.DATES 
JOIN SAMDAT3 ON samdat1.FLIGHT = samdat3.FLIGHT 
WHERE DELAY > 0 
ORDER BY DELAY DESC
""", conn)
print("Libname Sample 9b: Delayed International Flights in March")
print(df_delayed_flights_b)

# =========================
# LIBNAME Sample 9c
# =========================
df_delayed_flights_c = pd.read_sql_query("""
SELECT DISTINCT samdat1.FLIGHT, samdat1.DATES, DELAY 
FROM SAMDAT1 
FULL JOIN SAMDAT2 ON samdat1.FLIGHT = samdat2.FLIGHT 
FULL JOIN SAMDAT3 ON samdat1.FLIGHT = samdat3.FLIGHT 
ORDER BY DELAY DESC
""", conn)
print("Libname Sample 9c: Delayed International Flights in March")
print(df_delayed_flights_c)

# =========================
# LIBNAME Sample 9d
# =========================
df_delayed_flights_d = pd.read_sql_query("""
SELECT DISTINCT samdat1.FLIGHT, samdat1.DATES, DELAY 
FROM SAMDAT1 
JOIN SAMDAT2 ON samdat1.FLIGHT = samdat2.FLIGHT AND samdat1.DATES = samdat2.DATES 
JOIN SAMDAT3 ON samdat1.FLIGHT = samdat3.FLIGHT 
WHERE DELAY > 0 
ORDER BY DELAY DESC
""", conn)
print("Libname Sample 9d: Delayed International Flights in March")
print(df_delayed_flights_d)

# =========================
# LIBNAME Sample 10
# =========================
df_payrolls = pd.read_sql_query("""
SELECT IDNUM, SEX, JOBCODE, SALARY, BIRTH, HIRED 
FROM SAMDAT5 
UNION ALL 
SELECT * FROM SAMDAT6 
ORDER BY IDNUM, JOBCODE, SALARY
""", conn)
print("Libname Sample 10: Payrolls 1 & 2")
print(df_payrolls)

# =========================
# LIBNAME Sample 11
# =========================
# Assuming enginename is defined
enginename = 'ASTER'  # Example value
if enginename == 'ASTER':
    conn.execute("INSERT INTO SAMDAT8 VALUES (1588, 'NY', 'FA')")
else:
    conn.execute("INSERT INTO SAMDAT8 VALUES ('1588', 'NY', 'FA')")
df_samdat8_updated = pd.read_sql_query("SELECT * FROM SAMDAT8", conn)
print("Libname Sample 11: New Row in AIRLINE.SAMDAT8")
print(df_samdat8_updated)

# =========================
# LIBNAME Sample 12
# =========================
# Assuming enginename is defined
if enginename not in ['HAWQ', 'IMPALA']:
    conn.execute("DELETE FROM SAMDAT7 WHERE STATE='CT'")
df_samdat7_updated = pd.read_sql_query("SELECT * FROM SAMDAT7", conn)
print("Libname Sample 12: AIRLINE.SAMDAT7 After Deleting Connecticut Employees")
print(df_samdat7_updated)

# =========================
# LIBNAME Sample 13
# =========================
df_gtforty = pd.read_sql_query("""
SELECT LNAME AS lastname, FNAME AS firstname, SALARY AS Salary 
FROM SAMDAT7 a 
JOIN SAMDAT5 b ON a.IDNUM = b.IDNUM 
WHERE SALARY > 40000
""", conn)
df_gtforty['Salary'] = df_gtforty['Salary'].apply(lambda x: "${:,.2f}".format(x))
print("Libname Sample 13: Employees with salaries over $40,000")
print(df_gtforty)

# =========================
# LIBNAME Sample 14
# =========================
df_passengers = pd.read_sql_query("SELECT DATES, BOARDED FROM SAMDAT1", conn)
print("Libname Sample 14: Number of Passengers per Flight by Date")
print(df_passengers.groupby(['FLIGHT', 'DEST']).sum('BOARDED'))

# =========================
# LIBNAME Sample 15
# =========================
print("Libname Sample 15: Table Listing")
df_datasets = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
print(df_datasets)

# =========================
# LIBNAME Sample 16
# =========================
print("Libname Sample 16: Contents of the SAMDAT2 Table")
df_samdat2_contents = pd.read_sql_query("SELECT * FROM SAMDAT2", conn)
print(df_samdat2_contents)

# =========================
# LIBNAME Sample 17
# =========================
df_ranked = df_samdat2_contents.copy()
df_ranked['RANKING'] = df_ranked['DELAY'].rank(method='min', ascending=False)
print("Libname Sample 17: Ranking of Delayed Flights")
print(df_ranked)

# =========================
# LIBNAME Sample 17a
# =========================
df_temp = df_samdat2_contents.copy()
df_temp.to_sql('SAMTEMP', conn, if_exists='replace', index=False)
conn.execute("DROP TABLE IF EXISTS SAMTEMP")

# =========================
# LIBNAME Sample 18
# =========================
df_jobcode_count = pd.read_sql_query("SELECT JOBCODE, COUNT(*) AS count FROM SAMDAT5 GROUP BY JOBCODE", conn)
print("Libname Sample 18: Number of Employees by Jobcode")
print(df_jobcode_count)

# =========================
# LIBNAME Sample 19
# =========================
df_samdat5 = pd.read_sql_query("SELECT * FROM SAMDAT5", conn)
df_samdat6 = pd.read_sql_query("SELECT * FROM SAMDAT6", conn)
df_samdat5 = pd.concat([df_samdat5, df_samdat6]).drop_duplicates()
print("Libname Sample 19: SAMAT5 After Appending SAMDAT6")
print(df_samdat5)

# =========================
# LIBNAME Sample 20
# =========================
df_invoice_freq = pd.read_sql_query("SELECT COUNTRY, COUNT(INVNUM) AS count FROM SAMDAT9 GROUP BY COUNTRY", conn)
print("Libname Sample 20: Invoice Frequency by Country")
print(df_invoice_freq)

# =========================
# LIBNAME Sample 21
# =========================
df_notpaid = pd.read_sql_query("""
SELECT INVNUM, BILLEDTO, AMTINUS, BILLEDON 
FROM (SELECT PAIDON, BILLEDON, INVNUM, AMTINUS, BILLEDTO FROM SAMDAT9 LIMIT 5) 
WHERE PAIDON IS NULL AND AMTINUS >= 300000.00
""", conn)
df_notpaid['AMTINUS'] = df_notpaid['AMTINUS'].apply(lambda x: "${:,.2f}".format(x))
print("Libname Sample 21: High Bills--Not Paid")
print(df_notpaid)

# =========================
# LIBNAME Sample 22
# =========================
df_emp_csr = pd.read_sql_query("SELECT * FROM SAMDAT10 WHERE dept IN ('CSR010', 'CSR011', 'CSR004')", conn)
df_family_members = pd.read_sql_query("""
SELECT samdat13.LASTNAME, samdat13.FIRSTNAM, samdat13.EMPID, samdat13.FAMILYID, samdat13.GENDER, samdat13.DEPT, samdat13.HIREDATE 
FROM emp_csr 
JOIN samdat13 ON emp_csr.EMPID = samdat13.FAMILYID
""", conn)
print("Libname Sample 22: Interns Who Are Family Members of Employees")
print(df_family_members)

# =========================
# LIBNAME Sample 23
# =========================
df_flight_info = pd.read_sql_query("SELECT * FROM SAMDAT1 WHERE dest='WAS'", conn)
print("Libname Sample 23: FedSql Dictionary Tables")
print(df_flight_info)

# =========================
# LIBNAME Sample 24
# =========================
# Create and insert into SAMTEMP
conn.execute("""
CREATE TABLE SAMTEMP (col1 INTEGER, TAB1_C1 TEXT, col2 INTEGER, col3 INTEGER)
""")
conn.execute("INSERT INTO SAMTEMP VALUES (101, 'pup', 103, 104)")
df_samtemp = pd.read_sql_query("SELECT * FROM SAMTEMP", conn)
print("Libname Sample 24: Passthru With Connect Using")
print(df_samtemp)

# Clean up
conn.execute("DROP TABLE SAMTEMP")
conn.close()
```