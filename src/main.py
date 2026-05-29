from fastapi import FastAPI
from src.database import create_users_table
from src.users.router import router as user_router

app = FastAPI(
    title="MVC User Management System",
    description="""
    User Management System developed using FastAPI,
    SQLite, and MVC Architecture.

    Features:
    - User Registration
    - User Search
    - User Validation
    - SQLite Database Storage
    """,
    version="1.0.0",
)

create_users_table()

app.include_router(user_router, prefix="/api", tags=["users"])

@app.get("/", tags=["health"])
def root():
    """Health check endpoint."""
    return {"message": "MVC User Management System is running successfully!"}