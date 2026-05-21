import sqlite3
from db import queries

DATABASE = 'db/todo.db'


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row        # возвращает строки как словари
    conn.execute('PRAGMA foreign_keys = ON')  # SQLite не включает FK по умолчанию
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(queries.create_table_users)
    cursor.execute(queries.create_table_projects)
    cursor.execute(queries.create_table_tasks)
    conn.commit()
    conn.close()