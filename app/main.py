from fastapi import FastAPI
from app.routes import predict, postgresql,home

app = FastAPI()

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

app.include_router(home.router)  # sin prefijo
app.include_router(predict.router, prefix="/api")
app.include_router(postgresql.router, prefix="/api")
