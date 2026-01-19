# JWT Authentication with Dependency Injection

## 1️⃣ What is JWT (JSON Web Token)

JWT is a compact, URL-safe token used to securely transmit information between a client and a server. It is mainly used for authentication and authorization in modern web applications.

## 2️⃣ Why We Need JWT

Since HTTP/HTTPS is stateless, the server does not remember the client after a request is completed. JWT helps maintain user identity across multiple requests without storing session data on the server.

## 3️⃣ Structure of JWT

JWT consists of three parts separated by dots:

```
HEADER.PAYLOAD.SIGNATURE
```

Each part has a specific responsibility to ensure security, identity, and verification.

## 4️⃣ JWT Header

The header contains metadata about the token, such as the token type (JWT) and the cryptographic algorithm used for signing. It tells the server how the token should be verified.

## 5️⃣ JWT Payload

The payload contains claims (data) about the user, such as user ID, roles, and expiration time. It helps the server understand who the user is and what they are allowed to do. Payload data is encoded, not encrypted.

## 6️⃣ JWT Signature

The signature is created using the encoded header, encoded payload, and a secret key. It ensures that the token has not been tampered with and confirms that the token was issued by a trusted server.

## 7️⃣ What is a Payload

A payload is the data-carrying part of JWT that represents user identity and authorization details. It should never store sensitive information like passwords because it can be decoded by anyone.

## 8️⃣ Why Header + Payload + Signature Are Required

- Header defines the verification method
- Payload stores user identity
- Signature ensures integrity and trust
- Removing any one of them breaks the security or functionality of JWT.

## 9️⃣ Stateless Nature of JWT

JWT is stateless, meaning the server does not store session information. Every request carries the token, making the system scalable and suitable for distributed architectures.

## 🔟 Why JWT Alone Is Not Enough

Handling JWT logic directly inside routes can cause tight coupling, code duplication, and testing difficulties. This is why an additional pattern like Dependency Injection is needed.

## 1️⃣1️⃣ What is Dependency Injection (DI)

Dependency Injection is a design pattern where required components are provided to a function instead of being created inside it. This improves modularity, reusability, and testability.

## 1️⃣2️⃣ Why DI is Used with JWT

DI helps inject authentication and authorization logic into routes without tightly coupling them. It allows centralized JWT validation, cleaner code, and easier testing.

## 1️⃣3️⃣ DI vs Middleware

- Middleware runs globally for every request.
- Dependency Injection runs selectively for specific routes.
- DI is used when authentication or logic is needed only for certain endpoints.

## 1️⃣4️⃣ JWT + DI Mental Model 🧠

- JWT answers: Who is the user?
- DI answers: How does the route receive authentication logic?
- Together, they form a clean, secure, and scalable authentication system.

## 1️⃣5️⃣ Real-Life Analogies

- JWT → ID card used to identify a person
- Signature → Official seal preventing forgery
- DI → Hiring a specialist instead of learning everything yourself