import pandas as pd

# CHECK DBMS TABLE DROPPEDr
mydblib = pd.HDFStore('mydblib.h5')
mydblib.remove('DUBLKTAB')

# CREATE DATASET
DUBLKDAT = pd.DataFrame({
    'name': ['amy', 'bill', 'charlie', 'david', 'elinor', 'pearl', 'vera', 'frank', 'georgia', 'henry', 'joann', 'buddy'],
    'age': [3, 12, 35, 19, 42, 78, 96, 24, 1, 46, 27, 66],
    'sex': ['f', 'm', 'm', 'm', 'f', 'f', 'f', 'm', 'f', 'm', 'f', 'm'],
    'bdate': ['03/01/1985', '12/12/1977', '01/02/1953', '10/14/1969', '08/08/1945', '05/12/1922', '10/12/2000', '09/26/1963', '04/06/1987', '05/30/1942', '02/04/1961', '10/14/1932']
})

# CREATE DBMS TABLE WITH OPTIONS
DUBLKTAB = DUBLKDAT.copy()
DUBLKTAB.to_hdf('mydblib.h5', key='DUBLKTAB', mode='a', format='table', data_columns=True)

# Read Table
DUBLKTAB = pd.read_hdf('mydblib.h5', key='DUBLKTAB')
print(DUBLKTAB)
