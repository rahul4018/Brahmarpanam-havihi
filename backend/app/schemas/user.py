from pydantic import BaseModel
from pydantic import EmailStr


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    role: str

    model_config = {
        "from_attributes": True
    }