from src.database import get_db_connection

def insert_user(name: str, email: str) -> int:
    """Inserts a new user into the database and returns the generated ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email),
    )
    conn.commit()
    user_id: int = cursor.lastrowid
    conn.close()
    return user_id

def get_user_by_id(user_id: int):
    """Retrieves a user by their ID. Returns None if not found."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users() -> list:
    """Retrieves all users from the database ordered by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users ORDER BY id")
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(user_id: int, name: str, email: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET name = ?, email = ?
        WHERE id = ?
        """,
        (name, email, user_id)
    )

    conn.commit()

    updated_rows = cursor.rowcount

    conn.close()

    return updated_rows

def delete_user(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )

    conn.commit()

    deleted_rows = cursor.rowcount

    conn.close()

    return deleted_rows

def count_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) as total FROM users"
    )

    result = cursor.fetchone()

    conn.close()

    return result["total"]