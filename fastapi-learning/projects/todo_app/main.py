from fastapi import FastAPI, HTTPException
from typing import List
from .models import Todo, TodoIn

app = FastAPI(title="Todo API")

# In-memory storage for demo purposes
todos_db = []
current_id = 1


@app.get("/")
def read_root():
    return {"message": "Todo API"}


@app.get("/todos/", response_model=List[Todo])
def get_todos(skip: int = 0, limit: int = 100):
    """
    Get a list of todos with optional pagination
    """
    return todos_db[skip:skip + limit]


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    """
    Get a specific todo by ID
    """
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/todos/", response_model=Todo)
def create_todo(todo: TodoIn):
    """
    Create a new todo
    """
    global current_id
    new_todo = Todo(id=current_id, **todo.dict())
    todos_db.append(new_todo)
    current_id += 1
    return new_todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_in: TodoIn):
    """
    Update an existing todo
    """
    for idx, todo in enumerate(todos_db):
        if todo.id == todo_id:
            updated_todo = Todo(id=todo_id, **todo_in.dict())
            todos_db[idx] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """
    Delete a todo
    """
    global todos_db
    initial_length = len(todos_db)
    todos_db = [todo for todo in todos_db if todo.id != todo_id]
    if len(todos_db) == initial_length:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}