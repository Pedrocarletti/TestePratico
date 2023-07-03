from pydantic import BaseModel

class Usuario(BaseModel):
    name: str 
    password: str
    email: str

class Admin(BaseModel):
    username: str
    password: str


class Skin(BaseModel):
    filename: str
    contents: str
    rarity: str
    name: str
    value: int

    
    
