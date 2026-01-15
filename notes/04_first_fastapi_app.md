# Creating Your First FastAPI App

Let's build your first FastAPI application step by step. This will give you hands-on experience with the basics of FastAPI development.

## Minimal FastAPI Application

Let's start with the most basic FastAPI application:

This represents the simplest possible FastAPI application that returns a JSON response when accessing the root endpoint.

### Running Your App

Save the code as `main.py` and run it:

uvicorn main:app --reload

Then visit:
- `http://127.0.0.1:8000` - Your API endpoint
- `http://127.0.0.1:8000/docs` - Interactive API documentation (Swagger UI)
- `http://127.0.0.1:8000/redoc` - Alternative API documentation (ReDoc)

## Understanding the Components

### 1. Import Statement
This imports the FastAPI class from the fastapi module.

### 2. Create FastAPI Instance
Creates an instance of the FastAPI class. This is the main entry point for your API.

### 3. Path Operation Decorator
The decorator tells FastAPI that the function below should handle requests to the path `/` using a GET operation.

### 4. Path Operation Function
This is the function that will be called when a request is made to the specified path. The return value is automatically converted to JSON.

## Adding More Endpoints

Let's expand our application with more endpoints:

We can add multiple endpoints to handle different paths and HTTP methods. Each endpoint serves a specific purpose in your API.

## Path Parameters

Path parameters are declared as function parameters with type hints:

FastAPI automatically:
- Validates the path parameter
- Converts the parameter to the specified type
- Shows errors if validation fails

## Query Parameters

Query parameters are function parameters that are not path parameters:

These are optional parameters that appear in the URL after a question mark, useful for filtering, sorting, or pagination.

## More Path Operations

FastAPI supports all standard HTTP methods:

Each HTTP method serves a different purpose:
- GET: Retrieve data
- POST: Create new data
- PUT: Update existing data completely
- DELETE: Remove data
- PATCH: Partially update data

## Working with Different Data Types

FastAPI handles various Python data types automatically:

This includes basic types like integers, strings, booleans, as well as more complex types like enums and dates.

## Serving Static Files

FastAPI can serve static files using the `StaticFiles` class:

This is useful for serving images, CSS, JavaScript, or other static assets alongside your API.

## Error Handling

FastAPI provides automatic error handling for validation errors:

When validation fails, FastAPI automatically returns appropriate error responses with detailed information about what went wrong.

## Adding Metadata

You can add metadata to your FastAPI application:

Metadata helps document your API and provides useful information to consumers of your API.

## Complete Example

Here's a complete example combining everything we've learned:

This example demonstrates a full-featured API with multiple endpoints, proper error handling, and good organization. It includes CRUD operations for managing items and showcases many of FastAPI's capabilities.

Run this complete example with:
uvicorn complete_example:app --reload

This gives you a fully functional API with automatic documentation at `/docs`. You've now created your first complete FastAPI application!