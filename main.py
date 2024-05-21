from employee import Employee

def main():
    # Read employees from Excel file
    employees = Employee.read_from_excel('employee.xlsx')

    # Display information of all employees
    for employee in employees:
        employee.display_info()

if __name__ == "__main__":
    main()
