"""
Database module for Todo App
This is a simplified in-memory database implementation for demonstration purposes
"""

from typing import Dict, List, Optional
from .models import Todo

# In-memory storage for demo purposes
todos_db: Dict[int, Todo] = {}
current_id = 1


def get_next_id() -> int:
    """Generate the next available ID"""
    global current_id
    next_id = current_id
    current_id += 1
    return next_id


def get_todo(todo_id: int) -> Optional[Todo]:
    """Get a todo by ID"""
    return todos_db.get(todo_id)


def get_all_todos(skip: int = 0, limit: int = 100) -> List[Todo]:
    """Get all todos with optional pagination"""
    all_todos = list(todos_db.values())
    return all_todos[skip:skip + limit]


def create_todo(todo: Todo) -> Todo:
    """Create a new todo"""
    todos_db[todo.id] = todo
    return todo


def update_todo(todo_id: int, todo_data: Todo) -> Optional[Todo]:
    """Update an existing todo"""
    if todo_id not in todos_db:
        return None
    
    # Preserve the ID
    updated_todo = Todo(id=todo_id, **todo_data.dict(exclude={'id'}))
    todos_db[todo_id] = updated_todo
    return updated_todo


def delete_todo(todo_id: int) -> bool:
    """Delete a todo by ID"""
    if todo_id in todos_db:
        del todos_db[todo_id]
        return True
    return False