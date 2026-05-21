from fastapi import FastAPI
from contextlib import asynccontextmanager

from routers import task
from db import main_db


# тут надо подумать либо обьснить эту структуру запуска, или же оставить обычный
@asynccontextmanager
async def lifespan(app: FastAPI):
    main_db.init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(task.router)