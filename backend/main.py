from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from config import engine, SessionLocal
from models import Base, Tema, Votacion
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/votaciones/{tema_id}")
async def create_votacion(tema_id: int, a_favor: bool):
    """
    Crea una nueva votación para un tema dado.

    Args:
        tema_id (int): El ID del tema para el que se quiere crear la votación.
        a_favor (bool): Si el voto es a favor (True) o en contra (False).

    Returns:
        dict: Un diccionario con los detalles de la votación creada.

    Raises:
        HTTPException: Si el tema especificado no existe.
    """
    db = SessionLocal()
    try:
        tema = db.query(Tema).filter(Tema.id == tema_id).one()
    except:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    votacion = Votacion(a_favor=a_favor, tema_id=tema_id)
    db.add(votacion)
    db.commit()
    db.refresh(votacion)
    return {"id": votacion.id, "a_favor": votacion.a_favor, "tema_id": votacion.tema_id}


@app.get("/estadisticas/{tema_id}")
async def get_estadisticas(tema_id: int):
    """
    Obtiene las estadísticas de votación para un tema dado.

    Args:
        tema_id (int): El ID del tema para el que se quieren obtener las estadísticas.

    Returns:
        dict: Un diccionario con las estadísticas de votación del tema especificado.

    Raises:
        HTTPException: Si el tema especificado no existe.
    """
    db = SessionLocal()
    try:
        tema = db.query(Tema).filter(Tema.id == tema_id).one()
    except:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    votos_a_favor = (
        db.query(Votacion)
        .filter(Votacion.tema_id == tema_id, Votacion.a_favor == True)
        .count()
    )
    votos_en_contra = (
        db.query(Votacion)
        .filter(Votacion.tema_id == tema_id, Votacion.a_favor == False)
        .count()
    )
    return {
        "titulo": tema.titulo,
        "fecha_creacion": tema.fecha_creacion,
        "votos_a_favor": votos_a_favor,
        "votos_en_contra": votos_en_contra,
    }


@app.post("/temas")
async def create_tema(titulo: str, descripcion: str):
    """
    Crea un nuevo tema.

    Args:
        titulo (str): El título del tema.
        descripcion (str): La descripción del tema.

    Returns:
        dict: Un diccionario con los detalles del tema creado.
    """
    db = SessionLocal()
    tema = Tema(titulo=titulo, descripcion=descripcion, fecha_creacion=datetime.now())
    db.add(tema)
    db.commit()
    db.refresh(tema)
    return {
        "id": tema.id,
        "titulo": tema.titulo,
        "descripcion": tema.descripcion,
        "fecha_creacion": tema.fecha_creacion,
    }


@app.get("/temas")
async def get_temas():
    """
    Obtiene todos los temas.

    Returns:
        list: Una lista con los detalles de todos los temas.
    """
    db = SessionLocal()
    temas = db.query(Tema).all()
    return [
        {"id": tema.id, "titulo": tema.titulo, "fecha_creacion": tema.fecha_creacion}
        for tema in temas
    ]


@app.get("/temas/{tema_id}")
async def get_tema(tema_id: int):
    """
    Obtiene un tema dado su ID.

    Args:
        tema_id (int): El ID del tema que se quiere obtener.

    Returns:
        dict: Un diccionario con los detalles del tema especificado.

    Raises:
        HTTPException: Si el tema especificado no existe.
    """
    db = SessionLocal()
    try:
        tema = db.query(Tema).filter(Tema.id == tema_id).one()
    except:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    return {"id": tema.id, "titulo": tema.titulo, "fecha_creacion": tema.fecha_creacion}


@app.delete("/temas/{tema_id}")
async def delete_tema(tema_id: int):
    """
    Elimina un tema dado su ID.

    Args:
        tema_id (int): El ID del tema que se quiere eliminar.

    Returns:
        dict: Un diccionario con los detalles del tema eliminado.

    Raises:
        HTTPException: Si el tema especificado no existe.
    """
    db = SessionLocal()
    try:
        tema = db.query(Tema).filter(Tema.id == tema_id).one()
    except:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    db.delete(tema)
    db.commit()
    return {"id": tema.id, "titulo": tema.titulo, "fecha_creacion": tema.fecha_creacion}


@app.put("/temas/{tema_id}")
async def update_tema(tema_id: int, titulo: str):
    """
    Actualiza un tema dado su ID.

    Args:
        tema_id (int): El ID del tema que se quiere actualizar.
        titulo (str): El nuevo título del tema.

    Returns:
        dict: Un diccionario con los detalles del tema actualizado.

    Raises:
        HTTPException: Si el tema especificado no existe.
    """
    db = SessionLocal()
    try:
        tema = db.query(Tema).filter(Tema.id == tema_id).one()
    except:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    tema.titulo = titulo
    db.commit()
    db.refresh(tema)
    return {"id": tema.id, "titulo": tema.titulo, "fecha_creacion": tema.fecha_creacion}


if __name__ == "__main__":
    """Ejecutar el servidor y hacer que se recargue automáticamente cuando se detecten cambios en el código."""
    uvicorn.run(app, host="0.0.0.0", port=8000)
