from fastapi import FastAPI
from fastapi import HTTPException

from schema import TaskCreate, TaskResponse

app = FastAPI()

tasks: list[TaskResponse] = []
counter = 1


# GET список
@app.get('/tasks', response_model=list[TaskResponse])
def get_tasks():
    return tasks


# GET по id
@app.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail='Задача не найдена')


# POST создать
@app.post('/tasks', response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate):
    global counter
    task = TaskResponse(id=counter, title=data.title, completed=data.done)
    tasks.append(task)
    counter += 1
    return task


# DELETE удалить
@app.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail='Задача не найдена')
