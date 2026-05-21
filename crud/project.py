from db.main_db import get_connection
from db import queries


def get_all_projects():
    conn = get_connection()
    projects = conn.execute(queries.select_all_projects).fetchall()
    conn.close()
    return [dict(p) for p in projects]


def get_project_by_id(project_id: int):
    conn = get_connection()
    project = conn.execute(queries.select_project_by_id, (project_id,)).fetchone()
    conn.close()
    return dict(project) if project else None


def create_project(title: str, user_id: int):
    conn = get_connection()
    cursor = conn.execute(queries.insert_project, (title, user_id))
    conn.commit()
    project_id = cursor.lastrowid
    conn.close()
    return get_project_by_id(project_id)
