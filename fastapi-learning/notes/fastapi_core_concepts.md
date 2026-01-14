# 🌐 HTTP Status Codes (Core Backend Knowledge)

## 200 – OK
- **What**: Request succeeded
- **Why**: Server processed request correctly
- **How**: Used mainly for successful GET requests
- **Example**: Fetching user details

## 201 – Created
- **What**: Resource successfully created
- **Why**: Confirms new data was added
- **How**: Returned after POST requests
- **Example**: User registration

## 400 – Bad Request
- **What**: Server cannot understand request
- **Why**: Malformed JSON or invalid syntax
- **How**: Request fails before validation
- **Example**: Invalid JSON body

## 401 – Unauthorized
- **What**: Authentication required or failed
- **Why**: User not logged in or token missing
- **How**: No valid credentials provided
- **Example**: Accessing protected route without token

## 403 – Forbidden
- **What**: Access denied
- **Why**: User authenticated but lacks permission
- **How**: Role-based or permission-based denial
- **Example**: Normal user accessing admin route

## 404 – Not Found
- **What**: Resource does not exist
- **Why**: Wrong URL or missing data
- **How**: Route or resource not found
- **Example**: /users/999 when user doesn't exist

## 405 – Method Not Allowed
- **What**: HTTP method not supported
- **Why**: Wrong method for endpoint
- **How**: Route exists but method mismatch
- **Example**: POST on a GET-only endpoint

## 422 – Unprocessable Entity (FastAPI Special)
- **What**: Valid request but invalid data
- **Why**: Schema validation failed
- **How**: Pydantic detects type/field mismatch
- **Example**: Sending string instead of integer

### 🔑 Why FastAPI uses 422 instead of 400
- Request syntax is valid, but data doesn't match expected schema

## 500 – Internal Server Error
- **What**: Server crashed internally
- **Why**: Unhandled exception or bug
- **How**: Logic error, DB crash, runtime issue
- **Example**: Division by zero, DB connection failure

# 🔐 Sensitive Data (Security Concept)

## What is Sensitive Data?
Data that must not be exposed to clients due to security or privacy risks.

### Examples:
- Passwords / password hashes
- Tokens (JWT, API keys)
- Roles (is_admin)
- Personal data (Aadhaar, PAN, phone)

### Why it matters:
- Prevents data leaks
- Prevents privilege escalation
- Protects user privacy

# 📥 Request vs 📤 Response Models (FastAPI)

## Request Model
- Validates incoming data
- Prevents bad input
- Stops execution if invalid
- Returns 422 on failure

## Response Model
- Controls outgoing data
- Hides sensitive fields
- Ensures consistent responses

### 🔑 Key idea
- Request models protect the backend
- Response models protect the client

# ⚙️ FastAPI Internals & Request Lifecycle

## High-Level Flow
```
Client
 ↓
ASGI Server (Uvicorn)
 ↓
Routing
 ↓
Dependency Injection
 ↓
Request Parsing
 ↓
Pydantic Validation (422 if fails)
 ↓
Route Logic
 ↓
Response Model Filtering
 ↓
Serialization
 ↓
Client
```