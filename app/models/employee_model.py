from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from app.db import Base, SessionLocal
from app.db import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(200), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    department = Column(String(100), nullable=False, index=True)
    position = Column(String(150), nullable=True)
    phone = Column(String(20), nullable=True)


class EmployeeModel:
    @staticmethod
    def get_all():
        db = SessionLocal()
        employees = db.query(Employee).all()
        db.close()
        return employees

    @staticmethod
    def create(data):
        db = SessionLocal()
        emp = Employee(**data)
        db.add(emp)
        db.commit()
        db.refresh(emp)
        db.close()
        return emp

    @staticmethod
    def get_by_id(emp_id: int):
        db = SessionLocal()
        employee = db.query(Employee).filter(Employee.id == emp_id).first()
        db.close()
        return employee

    @staticmethod
    def delete(emp_id: int):
        db = SessionLocal()
        emp = db.query(Employee).filter(Employee.id == emp_id).first()
        if not emp:
            db.close()
            return None

        db.query(Attendance).filter(Attendance.employee_id == emp_id).delete()
        db.delete(emp)
        db.commit()
        db.close()
        return True

    @staticmethod
    def get_summary():
        db = SessionLocal()

        total_employees = db.query(Employee).count()

        today_present = (
            db.query(Attendance).filter(Attendance.status == "present").count()
        )

        today_absent = (
            db.query(Attendance).filter(Attendance.status == "absent").count()
        )

        department_count = db.query(
            func.count(func.distinct(Employee.department))
        ).scalar()

        db.close()

        return {
            "total_employees": total_employees,
            "present_today": today_present,
            "absent_today": today_absent,
            "department_count": department_count,
        }

    @staticmethod
    def update(emp_id, data):
        db = SessionLocal()

        emp = db.query(Employee).filter(Employee.id == emp_id).first()

        if not emp:
            db.close()
            return None

        for key, value in data.items():
            setattr(emp, key, value)

        db.commit()
        db.refresh(emp)
        db.close()

        return emp
