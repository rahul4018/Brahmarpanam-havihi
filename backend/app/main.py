from fastapi import FastAPI

from app.api.v1.auth.routes import router as auth_router

app = FastAPI(
    title="Brahmarpanam Havihi API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.get("/")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(
    auth_router,
    prefix="/api/v1"
)