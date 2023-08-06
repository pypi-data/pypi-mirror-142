from pydantic import BaseModel


class Author(BaseModel):
    alias: str
