"""pydantic models"""

from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    """Message"""

    message: str


class UserSchema(BaseModel):
    """User"""

    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    """UserPublic"""

    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    """UserPublic"""

    id: int
