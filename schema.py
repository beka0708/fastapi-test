from pydantic import BaseModel, Field
from typing import Optional


class TaskCreate(BaseModel):          # схема для входящего запроса
    title: str = Field(
        min_length=1,
        max_length=100,
        description='Название задачи'   # появится в Swagger
    )
    done: bool = Field(default=False)   # значение по умолчанию


class TaskResponse(BaseModel):        # схема для ответа
    id: int
    title: str
    completed: bool