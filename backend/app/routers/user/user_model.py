from uuid import UUID
from pydantic import BaseModel, Field

class UserModel(BaseModel):
    name: str
    username: str
    preferences: str
    password: str
    is_active: bool = False


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserAuth(BaseModel):
    username: str = Field(..., description="user username")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class UserOut(BaseModel):
    id: UUID
    username: str


class SystemUser(UserOut):
    password: str