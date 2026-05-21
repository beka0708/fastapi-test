from db.main_db import get_connection
from db import queries


def get_all_tasks():
    conn = get_connection()
    tasks = conn.execute(queries.select_all_tasks).fetchall()
    conn.close()
    return [dict(t) for t in tasks]


def get_task_by_id(task_id: int):
    conn = get_connection()
    task = conn.execute(queries.select_task_by_id, (task_id,)).fetchone()
    conn.close()
    return dict(task) if task else None


def create_task(title: str, project_id: int):
    conn = get_connection()
    cursor = conn.execute(queries.insert_task, (title, project_id))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return get_task_by_id(task_id)


def update_task(task_id: int, title: str, done: bool):
    conn = get_connection()
    conn.execute(queries.update_task, (title, done, task_id))
    conn.commit()
    conn.close()
    return get_task_by_id(task_id)


def delete_task(task_id: int):
    conn = get_connection()
    conn.execute(queries.delete_task, (task_id,))
    conn.commit()
    conn.close()