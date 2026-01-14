#!/usr/bin/env python3
"""
Helper script to start a FastAPI server with common configurations
"""

import argparse
import subprocess
import sys
import os


def start_server(project_path: str, reload: bool = True, host: str = "127.0.0.1", port: int = 8000):
    """
    Start a FastAPI server with given parameters
    """
    main_file = os.path.join(project_path, "main.py")
    
    if not os.path.exists(main_file):
        print(f"Error: {main_file} not found!")
        return False
    
    cmd = [
        "uvicorn",
        "main:app",
        f"--host={host}",
        f"--port={port}"
    ]
    
    if reload:
        cmd.append("--reload")
    
    try:
        print(f"Starting server: {' '.join(cmd)}")
        subprocess.run(cmd, cwd=project_path)
        return True
    except KeyboardInterrupt:
        print("\nServer stopped.")
        return True
    except Exception as e:
        print(f"Error starting server: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Start a FastAPI server")
    parser.add_argument("project_path", help="Path to the project directory containing main.py")
    parser.add_argument("--no-reload", action="store_true", help="Disable auto-reload")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to (default: 8000)")
    
    args = parser.parse_args()
    
    success = start_server(
        project_path=args.project_path,
        reload=not args.no_reload,
        host=args.host,
        port=args.port
    )
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()