from db.main_db import get_connection
from db import queries


def get_all_users():
    conn = get_connection()
    users = conn.execute(queries.select_all_users).fetchall()
    conn.close()
    return [dict(u) for u in users]


def get_user_by_id(user_id: int):
    conn = get_connection()
    user = conn.execute(queries.select_user_by_id, (user_id,)).fetchone()
    conn.close()
    return dict(user) if user else None


def create_user(name: str, email: str):
    conn = get_connection()
    cursor = conn.execute(queries.insert_user, (name, email))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return get_user_by_id(user_id)
