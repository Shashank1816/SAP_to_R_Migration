# BULKLOAD Sample 1

# CHECK DBMS TABLE DROPPED
rm(list = ls())  # Clear all variables from the workspace

# CREATE DATASET
DUBLKDAT <- data.frame(
  name = c("amy", "bill", "charlie", "david", "elinor", "pearl", "vera", "frank", "georgia", "henry", "joann", "buddy"),
  age = c(3, 12, 35, 19, 42, 78, 96, 24, 1, 46, 27, 66),
  sex = c("f", "m", "m", "m", "f", "f", "f", "m", "f", "m", "f", "m"),
  bdate = as.Date(c("1985-03-01", "1977-12-12", "1953-01-01", "1969-10-14", "1945-08-08", "1922-05-12", "2000-10-12", "1963-09-26", "1987-04-06", "1942-05-30", "1961-02-04", "1932-10-14"), format = "%Y-%m-%d")
)

# CREATE DBMS TABLE WITH OPTIONS
DUBLKTAB <- DUBLKDAT

# Read Table
print(DUBLKTAB)
