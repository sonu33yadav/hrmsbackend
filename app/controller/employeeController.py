from fastapi import Request
from app.models.employee_model import EmployeeModel


async def getEmployees():
    employees = EmployeeModel.get_all()
    return {"status": True, "message": "Employee List Fetched", "data": employees}


async def createEmployee(data):
    emp = EmployeeModel.create(data)
    return {"status": True, "message": "Employee Added SucessFully", "data": emp}


async def getEmployeeById(emp_id: int):
    emp = EmployeeModel.get_by_id(emp_id)

    if not emp:
        return {"status": False, "message": "Employee not found"}

    return {"status": True, "message": "Employee List Fetched", "data": emp}


async def deleteEmployee(emp_id: int):
    result = EmployeeModel.delete(emp_id)

    if not result:
        return {"status": False, "message": "Employee not found"}

    return {"status": True, "message": "Employee deleted"}


async def getEmployeeSummary():
    summary = EmployeeModel.get_summary()

    return {"status": True, "message": "Employee Summery Found", "data": summary}


async def updateEmployee(emp_id, data):
    emp = EmployeeModel.update(emp_id, data)

    if not emp:
        return {"status": False, "message": "Employee not found"}

    return {"status": True, "message": "Employee updated", "data": emp}
