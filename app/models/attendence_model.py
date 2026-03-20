from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.db import Base, SessionLocal


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(50), nullable=False)


class AttendanceModel:

    @staticmethod
    def get_all(date=None, employee_id=None):
        from app.models.employee_model import Employee

        db = SessionLocal()
        query = db.query(
            Attendance.id,
            Attendance.employee_id,
            Attendance.date,
            Attendance.status,
            Employee.full_name.label("employee_name"),
        ).join(Employee, Attendance.employee_id == Employee.id)

        if date:
            query = query.filter(Attendance.date == date)

        if employee_id:
            query = query.filter(Attendance.employee_id == employee_id)

        records = query.all()
        db.close()
        return records

    @staticmethod
    def get_by_employee(employee_id: int, date=None):
        db = SessionLocal()
        query = db.query(Attendance).filter(Attendance.employee_id == employee_id)

        if date:
            query = query.filter(Attendance.date == date)

        records = query.all()
        db.close()
        return records

    @staticmethod
    def mark_attendance(data):
        db = SessionLocal()

        existing = (
            db.query(Attendance)
            .filter(
                Attendance.employee_id == data["employee_id"],
                Attendance.date == data["date"],
            )
            .first()
        )

        if existing:
            existing.status = data["status"]
            db.commit()
            db.refresh(existing)
            db.close()
            return existing

        record = Attendance(**data)
        db.add(record)
        db.commit()
        db.refresh(record)
        db.close()
        return record

    @staticmethod
    def delete(attendance_id: int):
        db = SessionLocal()
        record = db.query(Attendance).filter(Attendance.id == attendance_id).first()

        if not record:
            db.close()
            return None

        db.delete(record)
        db.commit()
        db.close()
        return True

    @staticmethod
    def update(att_id, data):
        db = SessionLocal()

        record = db.query(Attendance).filter(Attendance.id == att_id).first()

        if not record:
            db.close()
            return None

        for key, value in data.items():
            setattr(record, key, value)

        db.commit()
        db.refresh(record)
        db.close()

        return record
