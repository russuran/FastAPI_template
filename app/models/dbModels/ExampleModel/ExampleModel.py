from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.dbModels.EntityDB import EntityDB

class ExampleModel(EntityDB):
    __tablename__ = "example_model"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
