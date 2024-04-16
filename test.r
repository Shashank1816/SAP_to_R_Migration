# Create the dataset
efh <- data.frame(
  cond = c('A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B'),
  test = c(0.71, 0.82, 0.82, 0.76, 0.76, 0.71, 0.71, 0.82, 0.65, 0.53, 0.88, 0.59, 0.76, 0.59, 0.65),
  msat = c(650, 710, 510, 590, 510, 730, 570, 780, 690, 710, 780, 690, 730, 700, 740)
)
# Print the dataset
print(efh)

# Perform t-test
t_test <- t.test(test ~ cond, data = efh)
t_test

# # Define a simple function
# add_numbers <- function(x, y) {
#   return(x + y)
# }

# Save the function to a shared object file
dyn.load("test.so")
