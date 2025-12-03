import pytest

def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee Id: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return result

if _name_ == "_main_":
    # Sample Input
    name = "Alice"
    emp_id = "E1001"
    department = "IT"
    salary = 5500

    print(employee_details(name, emp_id, department, salary))
