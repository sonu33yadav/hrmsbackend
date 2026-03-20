from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class EmployeeBase(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=200)
    email: EmailStr
    department: str = Field(..., min_length=1, max_length=100)
    position: Optional[str] = None
    phone: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=2, max_length=200)
    email: Optional[EmailStr] = None
    department: Optional[str] = Field(None, min_length=1, max_length=100)
    position: Optional[str] = None
    phone: Optional[str] = None


class EmployeeResponse(EmployeeBase):
    id: int

    model_config = {"from_attributes": True}


class EmployeeUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    department: str | None = None
    position: str | None = None
    phone: str | None = None
