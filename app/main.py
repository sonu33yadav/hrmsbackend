from fastapi import FastAPI
from app.routers.employeeRouter import employeeRouter
from app.routers.attendanceRouter import attendanceRouter


app = FastAPI(
    title="HRMS Backend API",
    description="Employee and attendance management system",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employeeRouter, prefix="/api", tags=["Employee"])
app.include_router(attendanceRouter, prefix="/api", tags=["Attendence"])


@app.get("/")
def home():
    return {"message": "Iam on"}
