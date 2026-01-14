# Blog API

A simple blog API built with FastAPI that allows creating, reading, updating, and deleting blog posts.

## Features

- Create new blog posts with title, content, and author
- Retrieve lists of blog posts with pagination
- Get specific blog posts by ID
- Update existing blog posts
- Delete blog posts

## Endpoints

### GET /
- Description: Root endpoint
- Response: Welcome message

### GET /posts/
- Description: Get a list of blog posts
- Query Parameters:
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 20)
- Response: Array of blog post items

### GET /posts/{post_id}
- Description: Get a specific blog post by ID
- Path Parameter:
  - `post_id`: The ID of the post to retrieve
- Response: Single blog post item or 404 error

### POST /posts/
- Description: Create a new blog post
- Request Body:
  - `title` (required): Title of the post
  - `content` (required): Content of the post
  - `author` (required): Author of the post
- Response: Created blog post item

### PUT /posts/{post_id}
- Description: Update an existing blog post
- Path Parameter:
  - `post_id`: The ID of the post to update
- Request Body:
  - `title` (required): Title of the post
  - `content` (required): Content of the post
  - `author` (required): Author of the post
- Response: Updated blog post item or 404 error

### DELETE /posts/{post_id}
- Description: Delete a blog post
- Path Parameter:
  - `post_id`: The ID of the post to delete
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