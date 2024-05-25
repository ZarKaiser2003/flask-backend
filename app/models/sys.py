from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from models import Base

class SysUsers(Base):
    __tablename__ = "sys_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    is_admin: Mapped[bool] = mapped_column(Boolean)

    def __repr__(self) -> str:
        res = f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, password={self.password!r}, is_admin={self.is_admin!r})"
        return res
