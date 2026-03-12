from pydantic import BaseModel

class AdminQuery(BaseModel):
    user_name: str
    password: str 
    query: dict