from fastapi import APIRouter, HTTPException
from schemas.project import ProjectCreate, ProjectResponse
import crud.project as crud


router = APIRouter(prefix='/projects', tags=['Projects'])


@router.get('/', response_model=list[ProjectResponse])
def get_projects():
    return crud.get_all_projects()


@router.get('/{project_id}', response_model=ProjectResponse)
def get_project(project_id: int):
    project = crud.get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail='Проект не найден')
    return project


@router.post('/', response_model=ProjectResponse, status_code=201)
def create_project(data: ProjectCreate):
    return crud.create_project(data.title, data.user_id)
