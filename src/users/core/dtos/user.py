from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: Optional[int]
    email: str
    hashed_password: bytes
    first_name: str
    last_name: str
    is_active: bool

    def __repr__(self):
        return f"""UserDTO (id={self.id}, email={self.email},
                first_name={self.first_name}, last_name={self.last_name},
                is_active={self.is_active}"""
