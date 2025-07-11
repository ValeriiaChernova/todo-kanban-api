from fastapi import FastAPI
from app.routers import task

app = FastAPI()

app.include_router(task.router)

@app.get("/")
def read_root():
    return {"message": "ToDo API is working"}

