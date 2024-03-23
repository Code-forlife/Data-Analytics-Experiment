# Load necessary library
library(readr)

# Read CSV file into a data frame
data <- read.csv("OneDrive/SPIT College/3)Class/Semester 6/8)DA/1)Experiment/10_/loan_data_1.csv")

# View the structure of the data frame
str(data)

# Summary statistics of the data
summary(data)

# View the first few rows of the data frame
head(data)

# View the last few rows of the data frame
tail(data)

# Accessing specific columns
# For example, to access the Loan_Status column
loan_status <- data$Loan_Status
