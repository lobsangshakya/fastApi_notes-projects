from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime
import asyncio
import json

app = FastAPI(title="Chat API")

# Simple in-memory storage for demo
messages_db = []
connected_clients: List[WebSocket] = []


class MessageBase(BaseModel):
    sender: str
    content: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    timestamp: datetime


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                # Remove disconnected clients
                self.disconnect(connection)


manager = ConnectionManager()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Chat API"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Create message object
            message = Message(
                id=len(messages_db) + 1,
                sender=message_data['sender'],
                content=message_data['content'],
                timestamp=datetime.now()
            )
            
            # Store message
            messages_db.append(message)
            
            # Broadcast to all connected clients
            await manager.broadcast(json.dumps({
                "id": message.id,
                "sender": message.sender,
                "content": message.content,
                "timestamp": message.timestamp.isoformat()
            }))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{message_data.get('sender', 'A user')} left the chat")


@app.get("/messages", response_model=List[Message])
def get_messages(skip: int = 0, limit: int = 50):
    """
    Get chat history
    """
    return messages_db[skip:skip + limit]


@app.post("/messages", response_model=Message)
def send_message(message: MessageCreate):
    """
    Send a message (alternative to WebSocket)
    """
    new_message = Message(
        id=len(messages_db) + 1,
        sender=message.sender,
        content=message.content,
        timestamp=datetime.now()
    )
    messages_db.append(new_message)
    return new_message