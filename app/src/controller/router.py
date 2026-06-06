from app.config.config import app

@app.get("/")
def template_page():
    return {}