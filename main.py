from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello World",
        "author": "Roslaan",
        "country": "Nigeria",
        "greeting": "Welcome to the FastAPI application!",
        "year": 2025
    }

@app.get("/message")
def read_message():
    return {
        "message": "Hello World",
        "author": "Roslaan",
        "country": "Nigeria",
        "additional_info": {
            "language": {"Yoruba", "English"},
            "purpose": "Demonstration of FastAPI capabilities"
        }
    }

@app.get("/about")
def read_about():
    return {
        "app_name": "FastAPI Example",
        "version": "1.0.0",
        "description": "A simple FastAPI application",
        "developer": {
            "name": "Abdulsomad Abdulwahab",
            "role": "Developer",
            "email": "abdulsomad005@gmail.com",
            "location": "Nigeria"
        }
    }

@app.get("/status")
def read_status():
    return {
        "status": "running",
        "uptime": "24 hours",
        "details": {
            "requests_served": 1024,
            "errors": 0,
            "last_restart": "2025-04-06T00:00:00Z"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




