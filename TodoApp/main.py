from fastapi import FastAPI
from models import Base
from database import engine
from auth_router import auth, todos

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(auth.router_app)
app.include_router(todos.router)