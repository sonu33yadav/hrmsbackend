# HRMS Backend

FastAPI backend for HRMS project with Employee and Attendance management.

## Tech Stack
- FastAPI
- SQLAlchemy
- Alembic
- MySQL
- Uvicorn

## Project Structure

```bash
hrmsbackend/
│
├── app/
│   ├── main.py
│   ├── db.py
│   ├── controller/
│   │   ├── employeeController.py
│   │   └── attendanceController.py
│   ├── models/
│   │   ├── employee_model.py
│   │   └── attendence_model.py
│   ├── routers/
│   │   ├── employeeRouter.py
│   │   └── attendanceRouter.py
│   └── schemas/
│       ├── employee_schema.py
│       └── attendance_schema.py
│
├── alembic/
├── alembic.ini
├── requirements.txt
└── README.md


### Employee
- `GET /employee`
- `POST /addEmployees`
- `PUT /updateEmployee/{id}`
- `DELETE /deleteEmployee/{id}`

---

### Attendance
- `GET /attendance`
- `GET /attendance/employee/{id}`
- `POST /markAttendence`
- `PUT /updateAttendance/{id}`
- `DELETE /deleteAttendance/{id}`

---

### Dashboard
- `GET /dashboard/stats`