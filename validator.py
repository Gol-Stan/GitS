from pydantic import BaseModel, EmailStr, Field, validator
import re


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64)

    @validator("username")
    def validate_username(cls, v):
        if not re.match(r"^[A-Za-z0-9_-]+$", v):
            raise ValueError("Username may contain only letters, numbers, '-', or '_'")
        return v

    @validator("email")
    def validate_email(cls, v):
        forbidden_domains = []
        domain = v.split("@")[-1]
        if domain in forbidden_domains:
            raise ValueError("Registration with this email domain is not allowed")
        return v

    @validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[@$!%*?&]", v):
            raise ValueError("Password must contain at least one special character (@, $, !, %, *, ?, &)")
        return v
