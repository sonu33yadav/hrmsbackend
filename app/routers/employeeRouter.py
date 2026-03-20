from fastapi import APIRouter, HTTPException
from app.controller import employeeController
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate


employeeRouter = APIRouter()


@employeeRouter.get("/employee")
async def getEmployees():
    try:
        return await employeeController.getEmployees()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@employeeRouter.post("/addEmployees")
async def addEmployee(emp: EmployeeCreate):
    try:
        return await employeeController.createEmployee(emp.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@employeeRouter.get("/getEmployeeDetail/{id}")
async def employee_by_id(id: int):
    try:
        return await employeeController.getEmployeeById(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@employeeRouter.delete("/deleteEmployee/{id}")
async def remove_employee(id: int):
    try:
        return await employeeController.deleteEmployee(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@employeeRouter.get("/employees/summary")
async def employee_summary():
    try:
        return await employeeController.getEmployeeSummary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@employeeRouter.put("/employees/{id}")
async def update_employee(id: int, emp: EmployeeUpdate):
    try:
        return await employeeController.updateEmployee(id, emp.dict(exclude_unset=True))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
