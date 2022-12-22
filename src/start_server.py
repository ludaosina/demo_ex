from settings import SQL_BASE, SERVER_HOST, SERVER_PORT
from server.sql_base.pharmacy_db import base_worker
from fastapi import APIRouter
from server.router import routers
from uvicorn import run

base_worker.create_base(SQL_BASE)

app = APIRouter()


@app.get("/")
def start_page():
    return "hello luda"


[app.include_router(router) for router in routers]


if __name__ == "__main__":
    run("start_server:app", host=SERVER_HOST, port=SERVER_PORT)
