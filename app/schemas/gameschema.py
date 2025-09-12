from pydantic import BaseModel

class GameSchema(BaseModel):
    name: str
    type : str