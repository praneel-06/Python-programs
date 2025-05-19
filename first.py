import pandas as pd

# Sample data
data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [50000, 55000, 60000, 62000, 70000, 72000]
}

df = pd.DataFrame(data)

print("🔸 Original DataFrame:")
print(df)

# Group by 'Department' and calculate average salary
avg_salary = df.groupby('Department')['Salary'].mean()

print("\n🔹 Average Salary by Department:")
print(avg_salary)