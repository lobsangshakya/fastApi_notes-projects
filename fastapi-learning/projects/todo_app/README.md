# Todo App

A simple todo list API built with FastAPI.

## Features

- Create, read, update, and delete todos
- Mark todos as completed
- Pagination support for listing todos

## Endpoints

### GET /
- Description: Root endpoint
- Response: Welcome message

### GET /todos/
- Description: Get a list of todos
- Query Parameters:
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 100)
- Response: Array of todo items

### GET /todos/{todo_id}
- Description: Get a specific todo by ID
- Path Parameter:
  - `todo_id`: The ID of the todo to retrieve
- Response: Single todo item or 404 error

### POST /todos/
- Description: Create a new todo
- Request Body:
  - `title` (required): Title of the todo
  - `description` (optional): Description of the todo
  - `completed` (optional): Completion status (default: false)
- Response: Created todo item

### PUT /todos/{todo_id}
- Description: Update an existing todo
- Path Parameter:
  - `todo_id`: The ID of the todo to update
- Request Body:
  - `title` (required): Title of the todo
  - `description` (optional): Description of the todo
  - `completed` (optional): Completion status
- Response: Updated todo item or 404 error

### DELETE /todos/{todo_id}
- Description: Delete a todo
- Path Parameter:
  - `todo_id`: The ID of the todo to delete
- Response: Success message or 404 error

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Visit `http://localhost:8000/docs` to view the interactive API documentation.