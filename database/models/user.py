from pydantic import Field

from .base import Base


class User(Base):
    id: int
    name: str
    username: str
    lang: str = Field(default="en")
    status: str = Field(default="user")
    

User.set_collection("user")
