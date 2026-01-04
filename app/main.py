from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import auth

app = FastAPI(
    title="Biomachine",
    docs_url=None,
    redoc_url=None,
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

app.include_router(auth.router)