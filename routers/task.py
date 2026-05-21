from fastapi import APIRouter, HTTPException
from schemas.task import TaskCreate, TaskResponse
import crud.task as crud


router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.get('/', response_model=list[TaskResponse])
def get_tasks():
    return crud.get_all_tasks()


@router.get('/{task_id}', response_model=TaskResponse)
def get_task(task_id: int):
    task = crud.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Задача не найдена')
    return task


@router.post('/', response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate):
    return crud.create_task(data.title, data.project_id)


@router.put('/{task_id}', response_model=TaskResponse)
def update_task(task_id: int, data: TaskCreate):
    task = crud.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Задача не найдена')
    return crud.update_task(task_id, data.title, data.done)


@router.delete('/{task_id}', status_code=204)
def delete_task(task_id: int):
    task = crud.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Задача не найдена')
    crud.delete_task(task_id)

