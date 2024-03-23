# Load necessary libraries
library(ggplot2)
# Read CSV file into a data frame
data <- read.csv("OneDrive/SPIT College/3)Class/Semester 6/8)DA/1)Experiment/10_/loan_data_1.csv")

# Graph for Loan Status
ggplot(data, aes(x = Loan_Status)) +
  geom_bar(fill = "blue") +
  labs(title = "Loan Approval Status", x = "Loan Status", y = "Count")

# Graph for Applicant Income vs Loan Amount
ggplot(data, aes(x = ApplicantIncome, y = LoanAmount)) +
  geom_point(color = "red") +
  labs(title = "Applicant Income vs Loan Amount", x = "Applicant Income", y = "Loan Amount")

# Graph for Property Area
ggplot(data, aes(x = Property_Area, fill = Loan_Status)) +
  geom_bar() +
  labs(title = "Loan Approval Status by Property Area", x = "Property Area", y = "Count") +
  scale_fill_manual(values = c("green", "red"))
