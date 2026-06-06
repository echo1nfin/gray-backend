<<<<<<< HEAD
import fastapi

if __name__ == "__main__":
=======
import uvicorn
from src.config.config import app

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
>>>>>>> 2be8cb431367c26a3d818cd860fc449078174944
