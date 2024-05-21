import pandas as pd

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: ${self.salary}")

    @staticmethod
    def read_from_excel(file_path):
        employees = []
        try:
            df = pd.read_excel(file_path)
            for _, row in df.iterrows():
                employees.append(Employee(row['emp_id'], row['name'], row['department'], row['salary']))
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return employees
