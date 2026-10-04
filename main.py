from fastapi import FastAPI, HTTPException
from employee_dto import EmployeeDTO
from employee_service import (
    get_all_employees,
    get_employee,
    add_employee,
    update_employee,
    delete_employee
)

app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management API"
    }


# GET /employees
@app.get("/employees")
def get_employees():
    return get_all_employees()


# GET /employees/{id}
@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):

    employee = get_employee(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# POST /employees
@app.post("/employees", status_code=201)
def create_employee(employee: EmployeeDTO):

    return add_employee(employee)


# PUT /employees/{id}
@app.put("/employees/{employee_id}")
def update_employee_by_id(
    employee_id: int,
    employee: EmployeeDTO
):

    updated_employee = update_employee(
        employee_id,
        employee
    )

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee


# DELETE /employees/{id}
@app.delete("/employees/{employee_id}")
def remove_employee(employee_id: int):

    deleted_employee = delete_employee(employee_id)

    if deleted_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee": deleted_employee
    }