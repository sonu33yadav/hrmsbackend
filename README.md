# HRMS Backend

## Project Overview
This is a FastAPI-based backend for a Human Resource Management System (HRMS). It provides APIs to manage employees, track attendance, and generate dashboard statistics.

## Tech Stack Used
- Python
- FastAPI
- SQLAlchemy
- Alembic
- MySQL
- Uvicorn

## Steps to Run the Project Locally

1. Clone the repository
git clone <backend-repo-url>
cd hrmsbackend

2. Create virtual environment
python -m venv venv

3. Activate virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Configure database in app/db.py
DATABASE_URL = "mysql+pymysql://username:password@host:3306/dbname"

6. Run migrations
alembic upgrade head

7. Start server
python -m uvicorn app.main:app --reload

8. Open API docs
http://127.0.0.1:8000/docs

## API Endpoints

Employee APIs
GET /api/employee
POST /api/addEmployees
PUT /api/updateEmployee/{id}
DELETE /api/deleteEmployee/{id}

Attendance APIs
GET /api/attendance
GET /api/attendance/employee/{id}
POST /api/markAttendence
PUT /api/updateAttendance/{id}
DELETE /api/deleteAttendance/{id}

Dashboard API
GET /api/dashboard/stats

## Assumptions / Limitations
- API naming is custom (not fully REST standard)
- No authentication implemented
- No pagination for large datasets
- Basic error handling
- Date handled as string in some cases
- No role-based access control

## Author
Sonu Yadav