from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    user_id: int


class ProjectResponse(BaseModel):
    id: int
    title: str
    user_id: int
