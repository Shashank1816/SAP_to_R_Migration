
import pandas as pd

# Create DataFrame
data = {
    'name': ['amy', 'bill', 'charlie', 'david', 'elinor', 'pearl', 'vera', 'frank', 'georgia', 'henry', 'joann', 'buddy'],
    'age': [3, 12, 35, 19, 42, 78, 96, 24, 1, 46, 27, 66],
    'sex': ['f', 'm', 'm', 'm', 'f', 'f', 'f', 'm', 'f', 'm', 'f', 'm'],
    'bdate': ['030185', '121277', '010253', '101469', '080845', '051222', '101200', '092663', '040687', '053042', '020461', '101432']
}
df = pd.DataFrame(data)

# Write DataFrame to CSV file
df.to_csv('DUBLKDAT.csv', index=False)

# Read CSV file into DataFrame
df = pd.read_csv('DUBLKDAT.csv')

# Print DataFrame
print(df)
