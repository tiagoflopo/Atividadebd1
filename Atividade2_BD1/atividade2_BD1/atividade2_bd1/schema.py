from pydantic import BaseModel

from datetime import date

class UserInfos(BaseModel):
    name: str
    cpf: int
    birth_date: date
    senha: str


class UserID(UserInfos):
    id: int


class UserPublic(BaseModel):
    id: int
    name: str
    birth_date: date


class UserList(BaseModel):
    users: list[UserPublic]