from fastapi import FastAPI

app = FastAPI()

# Список задач
tasks = [
    {
        "id": 1,
        "title": "Купить продукты",
        "completed": True
    },
    {
        "id": 2,
        "title": "Сходить на курсы",
        "completed": False
    },
]


# Вызов: GET /tasks?completed=true
# Query-параметр: /tasks?completed=true — опциональный, фильтр
@app.get("/tasks")
def get_tasks(completed: bool = None):
    """Запрос на получение задач"""
    if completed is None:
        return tasks
    return [t for t in tasks if t['completed'] == completed]


# Вызов: GET /tasks/2
# Path-параметр: /tasks/{id} — обязательный, часть пути
@app.get('/tasks/{task_id}')
def get_task(task_id: int):
    "Запрос на получение одной задачи по ID"
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": 'Задача не найдена'}       # Пока что без HTTPException



@app.post("/task")
def create_task(title: str):
    """Запрос на создание задачи"""
    new_task = {
        'id': len(tasks) + 1,
        'title': title,
        'completed': False
    }
    tasks.append(new_task)
    return new_task

