from fastapi import APIRouter, HTTPException
from app.controller import attendanceController
from app.schemas.attendance_schema import AttendanceCreate, AttendanceUpdate

attendanceRouter = APIRouter()


@attendanceRouter.get("/attendance")
async def attendance(date: str = None, employeeId: int = None):
    try:
        return await attendanceController.getAttendance(date, employeeId)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@attendanceRouter.get("/attendance/employee/{id}")
async def attendance_by_employee(id: int, date: str = None):
    try:
        return await attendanceController.getAttendanceByEmployee(id, date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@attendanceRouter.post("/markAttendence")
async def create_attendance(payload: AttendanceCreate):
    try:
        return await attendanceController.markAttendance(payload.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@attendanceRouter.delete("/deleteAttendance/{id}")
async def remove_attendance(id: int):
    try:
        return await attendanceController.deleteAttendance(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@attendanceRouter.put("/updateAttendance/{id}")
async def update_attendance(id: int, payload: AttendanceUpdate):
    try:
        return await attendanceController.updateAttendance(
            id, payload.model_dump(exclude_unset=True)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
