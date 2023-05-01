from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from config import Base


class Tema(Base):
    __tablename__ = "tema"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, unique=True, index=True)
    descripcion = Column(String)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    votaciones = relationship("Votacion", back_populates="tema")


class Votacion(Base):
    __tablename__ = "votacion"

    id = Column(Integer, primary_key=True, index=True)
    a_favor = Column(Boolean)
    fecha_votacion = Column(DateTime, default=datetime.utcnow)

    tema_id = Column(Integer, ForeignKey("tema.id"))

    tema = relationship("Tema", back_populates="votaciones")
