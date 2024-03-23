
# Load necessary library
library(readr)
# Read CSV file into a data frame
data <- read.csv("OneDrive/SPIT College/3)Class/Semester 6/8)DA/1)Experiment/10_/loan_data_1.csv")


# Check for missing values
missing_values <- sum(is.na(data))

if (missing_values > 0) {
  # Remove rows with missing values
  data <- na.omit(data)
  print("Warning: Missing values found in the dataset and have been removed.")
}

# Calculate mean, variance, and standard deviation
mean_values <- colMeans(data[, c("ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term")], na.rm = TRUE)
variance_values <- sapply(data[, c("ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term")], var, na.rm = TRUE)
std_dev_values <- sapply(data[, c("ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term")], sd, na.rm = TRUE)

# Print the results
print("Mean values:")
print(mean_values)
print("Variance values:")
print(variance_values)
print("Standard deviation values:")
print(std_dev_values)

