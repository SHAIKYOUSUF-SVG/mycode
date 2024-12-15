
import pandas as pd

# Example data
data = {
    'Name': ['John', 'Jane', 'Doe'],
    'Age': [28, 34, 29],
    'Department': ['HR', 'IT', 'Finance'],
    'Salary': [50000, 60000, 55000]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Exporting to Excel
df.to_excel('employee_report.xlsx', index=False)

print("Excel report generated successfully!")
