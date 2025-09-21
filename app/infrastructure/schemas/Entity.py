from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Entity(Base):
    __abstract__ = True