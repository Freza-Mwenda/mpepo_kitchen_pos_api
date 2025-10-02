#!/usr/bin/env python3
import subprocess
import sys


def install_requirements():
    """Install required packages"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def setup_mysql():
    """Setup MySQL database"""
    from configs.setup_mysql import create_database, test_connection
    
    print("Setting up MySQL database...")
    create_database()
    
    if not test_connection():
        print("❌ Please check your MySQL configuration in .env file")
        print("Required environment variables:")
        print("DB_HOST=localhost")
        print("DB_PORT=3306")
        print("DB_NAME=mpempo_pos")
        print("DB_USER=root")
        print("DB_PASSWORD=0955gang")
        return False
    
    return True

def run_server():
    """Start the FastAPI server"""
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    # Install requirements
    install_requirements()
    
    # Setup MySQL
    if setup_mysql():
        # Run server
        run_server()