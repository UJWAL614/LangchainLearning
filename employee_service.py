from employee_dto import EmployeeDTO


employees = [
    EmployeeDTO(
        id=1,
        name="Ujjwal",
        email="ujjwal@gmail.com",
        salary=80000,
        department="IT"
    ),
    EmployeeDTO(
        id=2,
        name="Rahul",
        email="rahul@gmail.com",
        salary=60000,
        department="HR"
    )
]


def get_all_employees():
    return employees


def get_employee(employee_id: int):
    for employee in employees:
        if employee.id == employee_id:
            return employee

    return None


def add_employee(employee: EmployeeDTO):
    employees.append(employee)
    return employee


def update_employee(employee_id: int, employee_data: EmployeeDTO):
    for index, employee in enumerate(employees):
        if employee.id == employee_id:
            employees[index] = employee_data
            return employee_data

    return None


def delete_employee(employee_id: int):
    for index, employee in enumerate(employees):
        if employee.id == employee_id:
            return employees.pop(index)

    return None