# Setup and Installation

Learn how to set up and install FastAPI for your development environment.

## Prerequisites

Before installing FastAPI, ensure you have:
- Python 3.7 or higher
- pip package manager (usually comes with Python)
- Virtual environment tools (recommended: venv or conda)

## Installing FastAPI

FastAPI can be installed using pip. It's recommended to use a virtual environment to avoid conflicts with other projects.

### 1. Create a Virtual Environment

Virtual environments help isolate your project dependencies from other Python projects on your system. This prevents conflicts between different versions of packages used in different projects.

On Windows:
fastapi-env\Scripts\activate

On macOS/Linux:
source fastapi-env/bin/activate

### 2. Install FastAPI and Uvicorn

FastAPI itself is lightweight, but you'll need an ASGI server to run your application. Uvicorn is a popular, lightning-fast ASGI server that works well with FastAPI.

Install the complete FastAPI package with all optional dependencies along with Uvicorn:
pip install "fastapi[all]" uvicorn[standard]

Alternatively, for minimal dependencies:
pip install fastapi uvicorn

### 3. Verify Installation

After installation, you can verify that FastAPI and its dependencies are properly installed by creating a simple test application.

## Recommended Project Structure

A well-organized project structure makes your code maintainable and easier to navigate as your application grows. Here's a recommended structure for FastAPI projects:

my-fastapi-project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   └── routers/
├── requirements.txt
├── .env
├── .gitignore
└── README.md

## Essential Dependencies

### Core Dependencies
When building a FastAPI application, you'll commonly use these packages:

- fastapi: The main framework
- uvicorn: ASGI server for running the application
- pydantic: Data validation and settings management
- python-multipart: For handling file uploads

### Development Dependencies
For development, testing, and code quality, consider these packages:

- pytest: Testing framework
- httpx: Client for testing HTTP requests
- black: Code formatter
- flake8: Code linter

## Using Virtual Environments

Virtual environments are crucial for Python development as they create isolated spaces for your project dependencies.

### With venv (recommended)
Python's built-in venv module is the most common way to create virtual environments.

Create virtual environment:
python -m venv venv

Activate on Windows:
venv\Scripts\activate

Activate on macOS/Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Deactivate when done:
deactivate

### With conda
If you're using Anaconda or Miniconda, you can create isolated environments with conda.

Create environment:
conda create -n fastapi-env python=3.10

Activate environment:
conda activate fastapi-env

Install dependencies:
pip install "fastapi[all]" uvicorn[standard]

## Development Tools

### Auto-reload during development
During development, it's helpful to have your server restart automatically when you make code changes. Uvicorn provides this functionality.

Enable auto-reload to restart server on code changes:
uvicorn app.main:app --reload

### Port and host configuration
By default, Uvicorn runs on port 8000, but you can customize this.

Specify custom port:
uvicorn app.main:app --reload --port 5000

Listen on all addresses:
uvicorn app.main:app --host 0.0.0.0 --port 8000

## Environment Variables

Environment variables help manage configuration that varies between development, staging, and production environments. Store sensitive information like API keys and database credentials in environment variables rather than hardcoding them.

Create a `.env` file for configuration:
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key-here
DEBUG=True

Install python-dotenv to load environment variables:
pip install python-dotenv

## Troubleshooting Common Issues

### Installation Errors
If you encounter issues during installation:

- Ensure Python 3.7+ is installed: `python --version`
- Upgrade pip: `pip install --upgrade pip`
- Check for conflicting packages

### Running with Different Python Versions
FastAPI works with Python 3.7+ but is optimized for newer versions. Consider using Python 3.10+ for the best experience.