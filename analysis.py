
import pandas as pd
import matplotlib.pyplot as plt

# Read job data
data = pd.read_csv("jobs.csv")

# Display job details
print("\nIT JOB MARKET DETAILS")
print(data)

# Total number of jobs
print("\nTotal Number of Jobs:", len(data))

# Average salary
print("\nAverage Salary:", data["Salary_LPA"].mean(), "LPA")

# Highest salary
print("\nHighest Salary:", data["Salary_LPA"].max(), "LPA")

# Lowest salary
print("\nLowest Salary:", data["Salary_LPA"].min(), "LPA")

# Job role count
print("\nJob Role Count:")
print(data["Job_Role"].value_counts())

# Create salary chart
plt.figure(figsize=(10, 5))
plt.bar(data["Job_Role"], data["Salary_LPA"])

plt.title("IT Job Salary Comparison")
plt.xlabel("Job Role")
plt.ylabel("Salary (LPA)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("salary_chart.png")

print("\nSalary chart saved successfully!")

plt.show()
