from fastapi import Request
from app.models.attendence_model import AttendanceModel


async def getAttendance(date=None, employee_id=None):
    records = AttendanceModel.get_all(date, employee_id)

    return {
        "status": True,
        "data": [
            {
                "id": row.id,
                "employee_id": row.employee_id,
                "date": str(row.date),
                "status": row.status,
            }
            for row in records
        ],
    }


async def getAttendanceByEmployee(employee_id: int, date=None):
    records = AttendanceModel.get_by_employee(employee_id, date)

    return {
        "status": True,
        "data": [
            {
                "id": row.id,
                "employee_id": row.employee_id,
                "date": str(row.date),
                "status": row.status,
            }
            for row in records
        ],
    }


async def markAttendance(data):
    record = AttendanceModel.mark_attendance(data)

    return {
        "status": True,
        "message": "Attendance saved",
        "data": {
            "id": record.id,
            "employee_id": record.employee_id,
            "date": str(record.date),
            "status": record.status,
        },
    }


async def deleteAttendance(attendance_id: int):
    result = AttendanceModel.delete(attendance_id)

    if not result:
        return {"status": False, "message": "Attendance not found"}

    return {"status": True, "message": "Attendance deleted"}


async def updateAttendance(att_id, data):
    record = AttendanceModel.update(att_id, data)

    if not record:
        return {"status": False, "message": "Attendance not found"}

    return {
        "status": True,
        "message": "Attendance updated",
        "data": {
            "id": record.id,
            "employee_id": record.employee_id,
            "date": str(record.date),
            "status": record.status,
        },
    }
