from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Employee Model
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float

# Temporary Database
employees = {}

# Create Employee
@app.post("/employees/")
def create_employee(employee: Employee):
    if employee.id in employees:
        raise HTTPException(status_code=400, detail="Employee already exists")

    employees[employee.id] = employee
    return {
        "message": "Employee created successfully",
        "employee": employee
    }

# Get All Employees
@app.get("/employees/")
def get_all_employees():
    return employees

# Get Employee By ID
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    if emp_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employees[emp_id]

# Update Employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, employee: Employee):
    if emp_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    employees[emp_id] = employee

    return {
        "message": "Employee updated successfully",
        "employee": employee
    }

# Delete Employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    if emp_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    deleted_employee = employees.pop(emp_id)

    return {
        "message": "Employee deleted successfully",
        "employee": deleted_employee
    }