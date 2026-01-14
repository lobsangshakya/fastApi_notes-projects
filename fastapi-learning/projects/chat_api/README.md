# Chat API

A real-time chat API built with FastAPI that supports WebSocket connections for real-time messaging.

## Features

- Real-time chat using WebSockets
- Message history storage and retrieval
- Multi-user chat support
- REST endpoint alternative for sending messages

## Endpoints

### GET /
- Description: Root endpoint
- Response: Welcome message

### WebSocket /ws
- Description: WebSocket endpoint for real-time chat
- Message Format (JSON):
  ```json
  {
    "sender": "username",
    "content": "message content"
  }
  ```
- Server broadcasts received messages to all connected clients

### GET /messages
- Description: Get chat history
- Query Parameters:
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 50)
- Response: Array of message items

### POST /messages
- Description: Send a message via REST (alternative to WebSocket)
- Request Body:
  - `sender` (required): Name of the message sender
  - `content` (required): Content of the message
- Response: Created message item

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Connect to the WebSocket endpoint at `ws://localhost:8000/ws` using a WebSocket client

4. Or visit `http://localhost:8000/docs` to view the interactive API documentation and test REST endpoints.

## WebSocket Client Example

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onopen = function(event) {
  console.log('Connected to chat');
  
  // Send a message
  ws.send(JSON.stringify({
    sender: 'Alice',
    content: 'Hello everyone!'
  }));
};

ws.onmessage = function(event) {
  console.log('Received:', event.data);
};
```