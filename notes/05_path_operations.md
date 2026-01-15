# Path Operations (GET, POST, PUT, DELETE)

Path operations are the core of any FastAPI application. They define how your API responds to different HTTP requests at specific URL paths.

## HTTP Methods Overview

FastAPI supports all standard HTTP methods, but the most commonly used are:

- **GET**: Retrieve data
- **POST**: Create data
- **PUT**: Update data completely
- **DELETE**: Remove data
- **PATCH**: Partially update data

## GET Operations

GET operations are used to retrieve data from the server.

### Basic GET Endpoint

The simplest form of a GET endpoint returns data when accessed at a specific path.

### GET with Path Parameters

Path parameters are captured using curly braces `{}`:

These are required parameters that become part of the URL path itself.

### GET with Query Parameters

Query parameters are function parameters that are not path parameters:

These are optional parameters that appear after a question mark in the URL, useful for filtering or pagination.

### GET with Multiple Query Parameters

Multiple query parameters allow for flexible querying and filtering of data.

### GET with Enum Path Parameters

Using enums for predefined values:

Enums restrict path parameters to a predefined set of values, providing better validation and documentation.

## POST Operations

POST operations are used to create new data on the server.

### Basic POST Endpoint

The simplest POST endpoint accepts data and creates a new resource.

### POST with Request Body

Using Pydantic models to define the request body:

Request models define the structure and validation rules for incoming data.

### POST with Response Model

Define what the response should look like:

Response models control what data is returned to clients and provide automatic documentation.

## PUT Operations

PUT operations are used to update existing data completely.

### Basic PUT Endpoint

PUT operations typically replace an entire resource with new data.

### PUT with Partial Updates Simulation

While PUT typically replaces the whole resource, you can simulate partial updates:

This approach allows updating only specific fields while preserving others.

## DELETE Operations

DELETE operations are used to remove data from the server.

### Basic DELETE Endpoint

DELETE operations remove resources and typically return confirmation of the deletion.

### DELETE with Confirmation Response

More sophisticated DELETE operations can return details about what was deleted.

## PATCH Operations

PATCH operations are used for partial updates.

### PATCH with Request Body

PATCH operations update only the fields that are provided in the request.

## Advanced Path Operation Features

### Response Codes

Specify custom response status codes:

Custom status codes provide more specific information about the outcome of operations.

### Multiple Path Operations for Same Path

Different HTTP methods for the same path:

This allows the same URL to handle different operations based on the HTTP method used.

### Path Operation Configuration

Configure path operations with additional parameters:

Additional configuration options help document and organize your API endpoints.

### Deprecating Endpoints

Mark endpoints as deprecated:

Deprecation warnings inform API consumers that endpoints will be removed in future versions.

## Complete Example with All Operations

Here's a complete example showing all path operations working together:

This comprehensive example demonstrates a well-structured API with proper error handling, validation, and clear separation of concerns. Each path operation follows RESTful conventions and provides appropriate responses.

This example demonstrates all major HTTP methods working together in a cohesive API. Each path operation has appropriate response models, status codes, and error handling.