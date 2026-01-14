from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Blog API")

# Simple in-memory storage for demo
posts_db = []
post_id_counter = 1


class PostBase(BaseModel):
    title: str
    content: str
    author: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime = None


@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API"}


@app.get("/posts/", response_model=List[Post])
def get_posts(skip: int = 0, limit: int = 20):
    """
    Get a list of blog posts
    """
    return posts_db[skip:skip + limit]


@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    """
    Get a specific post by ID
    """
    for post in posts_db:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts/", response_model=Post)
def create_post(post: PostCreate):
    """
    Create a new blog post
    """
    global post_id_counter
    new_post = Post(
        id=post_id_counter,
        title=post.title,
        content=post.content,
        author=post.author,
        created_at=datetime.now()
    )
    posts_db.append(new_post)
    post_id_counter += 1
    return new_post


@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post_update: PostCreate):
    """
    Update an existing post
    """
    for idx, post in enumerate(posts_db):
        if post.id == post_id:
            updated_post = Post(
                id=post_id,
                title=post_update.title,
                content=post_update.content,
                author=post_update.author,
                created_at=post.created_at,
                updated_at=datetime.now()
            )
            posts_db[idx] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    """
    Delete a post
    """
    global posts_db
    initial_length = len(posts_db)
    posts_db = [post for post in posts_db if post.id != post_id]
    if len(posts_db) == initial_length:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}