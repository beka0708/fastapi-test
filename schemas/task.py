from pydantic import BaseModel, Field


class TaskCreate(BaseModel):          # схема для входящего запроса
    title: str = Field(
        min_length=1,
        max_length=100,
        description='Название задачи'   # появится в Swagger
    )
    done: bool = Field(default=False)
    project_id: int


class TaskResponse(BaseModel):        # схема для ответа
    id: int
    title: str
    done: bool
    project_id: int