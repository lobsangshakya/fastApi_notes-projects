# Dependency Injection in FastAPI

## Dependency (Basic Concept)

A dependency is anything a function needs from outside to work.

Examples:

- Database connection
- Authenticated user
- Token
- Config values

If your code depends on something, that thing is a dependency.

## Dependency Injection (DI)

### What it is

A design pattern where dependencies are provided automatically

The function does not create what it needs

### Key idea

Don't create dependencies, receive them.

### Why DI exists

- Reduces tight coupling
- Improves code reuse
- Easier testing
- Cleaner architecture
- Better scalability

### FastAPI context

- FastAPI inspects function signatures
- Resolves dependencies before route logic
- Injects them per request
- If dependency fails → route does not run

## Real-World Analogy (Bank)

- Banker = route function
- Database expert = dependency
- Hiring the expert instead of learning DB = dependency injection
- Banker focuses only on business logic

## Why Dependency Injection is Important

- Centralized logic (auth, DB, permissions)
- Reusable components
- Safer and cleaner APIs
- Easy to replace or mock dependencies during testing

## Middleware

### What it is

- Code that runs for every request
- Applied globally
- Runs before and/or after route logic

### Used for

- Logging
- CORS
- Rate limiting
- Global authentication
- Adding headers

## Difference Between DI and Middleware

### Core difference (one line)

Middleware is global and automatic, DI is selective and intentional.

### Comparison Table

| Feature | Dependency Injection | Middleware |
|---------|---------------------|------------|
| Scope | Per route | Global |
| Applied | Only when requested | For every request |
| Purpose | Business logic & services | Cross-cutting concerns |
| Access to params | Full | Limited |
| Testability | Easy | Harder |
| Order control | High | Limited |

## Execution Order (FastAPI)

```
Request
 ↓
Middleware
 ↓
Routing
 ↓
Dependency Injection
 ↓
Route Logic
 ↓
Response
 ↓
Middleware
```

## Bank Analogy (Final & Correct)

- Security gate everyone passes → Middleware
- Calling a loan officer when needed → Dependency Injection
- Specialist called only for specific cases → DI

## Interview One-Liners (Memorize)

- Dependency: Something my function needs
- DI: Don't create, receive
- Middleware: Global and unavoidable
- DI vs Middleware: Middleware is automatic, DI is intentional

## Final 2-Line Interview Answer

Dependency Injection allows FastAPI to provide required services like authentication and database sessions directly to routes, keeping the code modular and testable. Middleware handles global concerns such as logging and security that apply to every request.