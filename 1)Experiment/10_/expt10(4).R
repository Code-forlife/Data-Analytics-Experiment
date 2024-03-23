# Load necessary library
library(stats)

# Assuming population parameters (replace with your actual values)
population_mean <- 50000  # Hypothetical population mean
population_sd <- 10000     # Hypothetical population standard deviation

# Check for missing values
missing_values <- sum(is.na(data))

if (missing_values > 0) {
  # Remove rows with missing values
  data <- na.omit(data)
  print("Warning: Missing values found in the dataset and have been removed.")
}

# Sample data
sample_mean <- mean(data$ApplicantIncome)  # Sample mean
sample_size <- length(data$ApplicantIncome)  # Sample size

# Calculate Z-score
z_score <- (sample_mean - population_mean) / (population_sd / sqrt(sample_size))

# Calculate p-value
p_value <- 2 * pnorm(-abs(z_score))  # for a two-tailed test

# Print Z-score and p-value
print(paste("Z-score:", z_score))
print(paste("p-value:", p_value))



# Assuming null hypothesis: population mean = 50000 (replace with your desired population mean)
population_mean <- 50000

# Perform one-sample t-test
t_test_result <- t.test(data$ApplicantIncome, mu = population_mean)

# Print t-test result
print(t_test_result)
