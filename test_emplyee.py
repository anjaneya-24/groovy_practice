import pytest
from employee import Employee

@pytest.fixture
def sample_data():
    return [
        Employee(1, 'John Doe', 'Engineering', 60000),
        Employee(2, 'Jane Smith', 'Marketing', 55000),
        Employee(3, 'Emily Davis', 'HR', 50000),
        Employee(4, 'Michael Brown', 'Sales', 65000)
    ]

def test_read_from_excel(sample_data):
    employees = Employee.read_from_excel('employees.xlsx')
    for emp, sample_emp in zip(employees, sample_data):
        assert emp.emp_id == sample_emp.emp_id
        assert emp.name == sample_emp.name
        assert emp.department == sample_emp.department
        assert emp.salary == sample_emp.salary

def test_display_info(capsys, sample_data):
    for emp in sample_data:
        emp.display_info()
    captured = capsys.readouterr()
    expected_output = (
        "ID: 1, Name: John Doe, Department: Engineering, Salary: $60000\n"
        "ID: 2, Name: Jane Smith, Department: Marketing, Salary: $55000\n"
        "ID: 3, Name: Emily Davis, Department: HR, Salary: $50000\n"
        "ID: 4, Name: Michael Brown, Department: Sales, Salary: $65000\n"
    )
    assert captured.out == expected_output
