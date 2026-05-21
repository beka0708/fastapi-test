# C-R-U-D


create_table_users = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
"""


create_table_projects = """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
"""


create_table_tasks = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT    NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0,
            project_id INTEGER NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
        )
"""


select_all_tasks = """
        SELECT t.id, t.title, t.done,
            p.title AS project_name
            FROM tasks t
            INNER JOIN projects p ON t.project_id = p.id
"""

select_task_by_id = """
    SELECT t.id, t.title, t.done, p.title AS project_name
    FROM tasks t
    INNER JOIN projects p ON t.project_id = p.id
    WHERE t.id = ?
"""

select_all_users = 'SELECT * FROM users'
select_user_by_id = 'SELECT * FROM users WHERE id = ?'
insert_user = 'INSERT INTO users (name, email) VALUES (?, ?)'

select_all_projects = 'SELECT * FROM projects'
select_project_by_id = 'SELECT * FROM projects WHERE id = ?'
insert_project = 'INSERT INTO projects (title, user_id) VALUES (?, ?)'

insert_task = 'INSERT INTO tasks (title, done, project_id) VALUES (?, 0, ?)'

update_task = 'UPDATE tasks SET title = ?, done = ? WHERE id = ?'

delete_task = 'DELETE FROM tasks WHERE id = ?'
