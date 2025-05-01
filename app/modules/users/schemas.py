from sqlmodel import SQLModel, BigInteger

class UserBase(SQLModel):
    id: int
    
class UserResponse(UserBase):
    query_id: str | None
    first_name: str
    last_name: str
    tg_username: str
    language_code: str
    photo_link: str
    
class UserCreate(UserResponse):
    pass

class UserUpdateFull(UserResponse):
    pass

class UserPartialUpdate(UserBase):
    query_id: str | None
    first_name: str | None
    last_name: str | None
    tg_username: str | None
    language_code: str | None
    photo_link: str | None