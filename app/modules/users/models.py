from sqlmodel import SQLModel, Field, BigInteger

class UserModel(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int = Field(primary_key=True)
    query_id: str | None
    first_name: str
    last_name: str
    tg_username: str
    language_code: str
    photo_link: str