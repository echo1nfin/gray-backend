import uvicorn
from src.config.config import app
from src.config.config import APP_URL

if __name__ == "__main__":
    uvicorn.run("main:app", host=APP_URL, port=8000, reload=True)