Here's the equivalent R code for the given SAS code:

```R
# Create the data frame
efh <- data.frame(
  cond = c("A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B"),
  test = c(0.71, 0.82, 0.82, 0.76, 0.76, 0.71, 0.71, 0.82, 0.65, 0.53, 0.88, 0.59, 0.76, 0.59, 0.65),
  msat = c(650, 710, 510, 590, 500, 730, 570, 780, 690, 710, 780, 690, 730, 700, 740)
)

# Add labels
attr(efh$cond, "label") <- "Experimental condition"
attr(efh$test, "label") <- "Fraction correct on post-test"
attr(efh$msat, "label") <- "Math SAT score"

# Print the data
print(efh)

# Perform t-test
t_test_result <- t.test(test ~ cond, data = efh)

# Print t-test results
print(t_test_result)
```

This R code creates the same dataset, adds labels to the variables, prints the data, and performs a t-test on the 'test' variable grouped by 'cond', which is equivalent to the operations in the original SAS code.