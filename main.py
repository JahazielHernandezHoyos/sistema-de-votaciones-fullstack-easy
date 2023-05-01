from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.database import SessionLocal, engine
from backend import main, crud, models, schemas

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")
templates = Jinja2Templates(directory="frontend")

models.Base.metadata.create_all(bind=engine)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = None
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(main.router)
app.include_router(crud.router, prefix="/users", tags=["users"])

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
