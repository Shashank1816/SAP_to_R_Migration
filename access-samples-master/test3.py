```python
import pandas as pd
import numpy as np

# Clean up
try:
    # Assuming mydblib is a DataFrame, we can drop the tables if they exist
    del mydblib['RDTAB78']
    del mydblib['CRTAB78A']
    del mydblib['CRTAB78B']
except KeyError:
    pass

# Create DBMS table
mydblib = {}
mydblib['RDTAB78'] = pd.DataFrame(np.array([(x, y) for x in range(1, 11) for y in range(1, 11)]), columns=['x', 'y'])

# Create tables without direct execution
CRTAB78A_noexe = mydblib['RDTAB78'][mydblib['RDTAB78']['x'] > 5].sort_values(by='y')[['y']]
CRTAB78B_noexe = mydblib['RDTAB78'][mydblib['RDTAB78']['x'] > 5]['y'].drop_duplicates().sort_values()

# Clean up
del mydblib['CRTAB78A']
del mydblib['CRTAB78B']

# Attempt create-table-as-select
CRTAB78A = mydblib['RDTAB78'][mydblib['RDTAB78']['x'] > 5].sort_values(by='y')[['y']]
CRTAB78B = mydblib['RDTAB78'][mydblib['RDTAB78']['x'] > 5]['y'].drop_duplicates().sort_values()

# Store results in work
work = {}
work['exeA'] = CRTAB78A
work['exeB'] = CRTAB78B

# Compare datasets
comparison_A = CRTAB78A.equals(CRTAB78A_noexe)
comparison_B = CRTAB78B.equals(CRTAB78B_noexe)

print("Comparison A equal:", comparison_A)
print("Comparison B equal:", comparison_B)
```