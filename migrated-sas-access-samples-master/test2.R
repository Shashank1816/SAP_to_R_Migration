Here's the equivalent R code for the given SAS code:

```r
# Global variables for bulkload
bl_path <- ""
bl_dbname <- ""
bl_host <- ""

# Create dataset
DUBLKDAT <- data.frame(
  name = c("amy", "bill", "charlie", "david", "elinor", "pearl", "vera", "frank", "georgia", "henry", "joann", "buddy"),
  age = c(3, 12, 35, 19, 42, 78, 96, 24, 1, 46, 27, 66),
  sex = c("f", "m", "m", "m", "f", "f", "f", "m", "f", "m", "f", "m"),
  bdate = as.Date(c("1985-03-01", "1977-12-12", "1953-01-02", "1969-10-14", "1945-08-08", "1922-05-12", "1900-10-12", "1963-09-26", "1987-04-06", "1942-05-30", "1961-02-04", "1932-10-14"))
)

# Create DBMS table with options
# Note: This part depends on the specific database connection method in R
# You may need to use a database-specific package like RPostgreSQL, RMySQL, etc.
# Example using DBI package:
library(DBI)
con <- dbConnect(your_db_driver, dbname = bl_dbname, host = bl_host)
dbWriteTable(con, "DUBLKTAB", DUBLKDAT)

# Read Table
print(DUBLKTAB)

# Cleanup
# Note: This also depends on your database connection method
dbRemoveTable(con, "DUBLKTAB")
dbDisconnect(con)
```

Note: The database operations (creating table, reading table, and cleanup) are approximated using generic DBI functions. You'll need to replace `your_db_driver` with the appropriate database driver and adjust the connection parameters as needed for your specific database setup.