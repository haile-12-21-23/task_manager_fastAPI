from fastapi import FastAPI

from .database import Base, engine
from .routers import tasks

app = FastAPI(title="Task Manager API")

app.include_router(tasks.router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Task Manager API Running"}
