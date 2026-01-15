# Request & Response Models using Pydantic

Pydantic is a powerful data validation and settings management library that integrates seamlessly with FastAPI. It uses Python type hints to validate data, making your APIs robust and reliable.

## Introduction to Pydantic

Pydantic is the backbone of data validation in FastAPI. It provides:
- Automatic data validation
- Type conversion
- Automatic documentation
- Easy serialization and deserialization

### Basic Pydantic Model

Pydantic models are classes that inherit from BaseModel and define the structure of your data using type hints.

Creating an instance validates the data according to the defined types and constraints.

## Request Models (Input Validation)

Request models define the structure of data that clients send to your API.

### Basic Request Model

Request models specify what data your API expects to receive from clients.

### Request Model with Default Values

Models can include default values for optional fields, making some data optional for clients.

### Request Model with Field Validation

Field validation adds constraints to ensure data meets specific requirements.

### Nested Request Models

Complex data structures can be represented using nested models.

### Advanced Field Options

Pydantic provides various field options for fine-grained control over validation and documentation.

## Response Models (Output Filtering)

Response models define the structure of data that your API returns to clients.

### Basic Response Model

Response models control what data is sent back to clients and provide automatic API documentation.

### Response Model with Computed Fields

Computed fields derive values from other fields or calculations.

### Using Response Model to Hide Sensitive Data

Response models are essential for security as they prevent sensitive information from being exposed.

## Advanced Pydantic Features

### Custom Validators

Custom validators allow you to implement complex validation logic that goes beyond basic type checking.

### Root Validators (for cross-field validation)

Root validators examine multiple fields together to enforce complex business rules.

### Using ConfigDict for Model Configuration

ConfigDict allows you to configure model-wide behavior and validation settings.

### Working with Different Data Types

Pydantic supports various Python data types including lists, dictionaries, dates, and custom types.

## Practical FastAPI Examples

### Complete Example with Request and Response Models

This example demonstrates a complete API implementation with proper separation between input validation and output formatting.

### Using Pydantic with Query Parameters

Pydantic models can also validate query parameters, providing consistent validation across your API.

## Best Practices

1. **Use specific response models**: Only return the data clients need
2. **Validate input thoroughly**: Use Pydantic's validation features
3. **Handle sensitive data**: Never return passwords or secrets in responses
4. **Use type hints consistently**: Makes your code more readable and maintainable
5. **Leverage Field for documentation**: Use Field to provide examples and descriptions
6. **Create separate models for input and output**: Different data may be needed for each
7. **Use ConfigDict for model-wide settings**: Configure model behavior consistently

Pydantic models are essential for building robust, well-documented FastAPI applications with automatic validation and serialization.