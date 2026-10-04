from pydantic import BaseModel


class EmployeeDTO(BaseModel):
    id: int
    name: str
    email: str
    salary: float
    department: str