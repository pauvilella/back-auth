from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: Optional[str]
    name: str
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]

    def __repr__(self):
        return f"""UserDTO(id={self.id}, name={self.name}, last_name={self.last_name},
            email={self.email}, password={self.password})"""
