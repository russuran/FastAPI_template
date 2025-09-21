from pydantic import BaseModel

class ExampleDTO(BaseModel):
    id: int
    text: str