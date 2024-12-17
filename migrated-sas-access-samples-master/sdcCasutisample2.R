# Load necessary libraries
library(DBI)
library(dplyr)

# Specify connection parameters
username <- "???????"
password <- "???????"
database <- "???????"
schema <- "???????"
dsn <- "???????"

# Create a database connection
con <- dbConnect(odbc::odbc(), 
                 .connection_string = paste0("Driver={ODBC Driver};",
                                              "Server=", dsn, ";",
                                              "Database=", database, ";",
                                              "Uid=", username, ";",
                                              "Pwd=", password, ";"))

# Create a sample data frame similar to the SAS data step
COLUMNSAMPLE <- data.frame(
  FLIGHT = c("114", "202", "219", "622", "132", "271", "302", "114", "202", "219", "622", "132"),
  DATES = c("01MAR98", "01MAR98", "01MAR98", "01MAR98", "01MAR98", "01MAR98", "01MAR98", "02MAR98", "02MAR98", "02MAR98", "02MAR98", "02MAR98"),
  DEPART = c("7:10", "10:43", "9:31", "12:19", "15:35", "13:17", "20:22", "7:10", "10:43", "9:31", "12:19", "15:35"),
  ORIG = c("LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA", "LGA"),
  DEST = c("LAX", "ORD", "LON", "FRA", "YYZ", "PAR", "WAS", "LAX", "ORD", "LON", "FRA", "YYZ"),
  MILES = c(2475, 740, 3442, 3857, 366, 3635, 229, 2475, 740, 3442, 3857, 366),
  BOARDED = c(172, 151, 198, 207, 115, 138, 105, 119, 120, 147, 176, 106),
  CAPACITY = c(210, 210, 250, 250, 178, 250, 180, 210, 210, 250, 250, 178)
)

# Display column information for the entire data frame
column_info <- data.frame(
  Column_Name = names(COLUMNSAMPLE),
  Data_Type = sapply(COLUMNSAMPLE, class),
  stringsAsFactors = FALSE
)
print(column_info)

# Display specific column information for selected variables
selected_vars <- c("FLIGHT", "DATES", "BOARDED", "CAPACITY")
selected_info <- column_info %>% filter(Column_Name %in% selected_vars)
print(selected_info)

# Alternative method of specifying variables to display
alternative_vars <- c("FLIGHT", "BOARDED")
alternative_info <- column_info %>% filter(Column_Name %in% alternative_vars)
print(alternative_info)

# Disconnect from the database
dbDisconnect(con)
