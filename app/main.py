from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates


from app.api.routes import auth

app = FastAPI(
    title="Biomachine",
    description="Biomachine is a platform for managing and analyzing biological data.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

templates = Jinja2Templates(directory="app/templates")

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)


app.include_router(auth.router)


@app.get("/")
def index_page():
    return "Hello, World!"

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000) 
