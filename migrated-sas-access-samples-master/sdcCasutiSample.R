
# Load necessary libraries
library(DBI)
library(dplyr)

# Specify connection parameters
username <- "???????"
password <- "???????"
database <- "???????"
schema <- "???????"
srctype <- "odbc"

# Create a connection string
con <- dbConnect(odbc::odbc(), 
                 .connection_string = paste0("Driver={ODBC Driver};",
                                              "Server=???????;",
                                              "Database=", database, ";",
                                              "Uid=", username, ";",
                                              "Pwd=", password, ";"))

# Create sample data frame
SAVESAMPLE <- data.frame(
  FLIGHT = c("114", "202", "219", "622", "132", "271", "302", "114", "202", "219", "622", "132"),
  DATES = c("01MAR98", "01MAR98", "01MAR98", "01MAR98", "01MAR98", "01MAR98", "01MAR98", "02MAR98", "02MAR98", "02MAR98", "02MAR98", "02MAR98"),
  DEPART = c("7:10", "10:43", "9:31", "12:19", "15:35", "13:17", "20:22", "7:10", "10:43", "9:31", "12:19", "15:35"),
  ORIG = c("LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA"),
  DEST = c("LAX", "ORD", "LON", "FRA", "YYZ", "PAR", "WAS", "LAX", "ORD", "LON", "FRA", "YYZ"),
  MILES = c(2475, 740, 3442, 3857, 366, 3635, 229, 2475, 740, 3442, 3857, 366),
  BOARDED = c(172, 151, 198, 207, 115, 138, 105, 119, 120, 147, 176, 106),
  CAPACITY = c(210, 210, 250, 250, 178, 250, 180, 210, 210, 250, 250, 178)
)

# Write the data frame to the database
dbWriteTable(con, "UTILLOADSAMPLE", SAVESAMPLE, overwrite = TRUE)

# Load the data into CAS (simulated here as a simple copy)
CASUTILLOAD <- dbReadTable(con, "UTILLOADSAMPLE")

# Print the loaded table
print(CASUTILLOAD)

# Save the data back to the database
dbWriteTable(con, "CASUTILSAVE", SAVESAMPLE, overwrite = TRUE)

# Verify the saved table
utilsave <- dbReadTable(con, "CASUTILSAVE")
print(utilsave)

# Display table metadata
metadata <- dbListFields(con, "SAVESAMPLE")
print(metadata)

# List tables in the database
tables <- dbListTables(con)
print(tables)

# Clean-up: Delete the table from the database
dbExecute(con, "DROP TABLE UTILLOADSAMPLE")

# Disconnect from the database
dbDisconnect(con)
