from sqlalchemy import Column, Float, LargeBinary
from .database import Base


class Image(Base):
    __tablename__ = "images"

    depth = Column(Float, primary_key=True, index=True)
    data = Column(LargeBinary)
