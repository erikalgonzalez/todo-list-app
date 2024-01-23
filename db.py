import sqlite3


def connect_to_db():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()

    # Drop the table if it exists
    conn.execute("DROP TABLE IF EXISTS tasks;")

    # Create the tasks table
    conn.execute("""
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        );
    """)

    conn.commit()
    print("Table created successfully")

    # Seed data for the tasks table
    tasks_seed_data = [
        ("Task 1",),
        ("Task 2",),
        ("Task 3",),
    ]

    conn.executemany(
        "INSERT INTO tasks (content) VALUES (?);", tasks_seed_data)
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()
