from sqlalchemy import Column, Integer, String

from app.infrastructure.schemas.Entity import Entity

class ExampleModel(Entity):
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True)
    text = Column(String)
