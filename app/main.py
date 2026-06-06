import uvicorn
from src.config.config import app
from src.config.config import APP_URL, APP_PORT

if __name__ == "__main__":
    uvicorn.run("main:app", host=APP_URL, port=APP_PORT, reload=True)