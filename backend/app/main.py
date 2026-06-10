from fastapi import FastAPI

app = FastAPI(
    title="Brahmarpanam Havihi API",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "Brahmarpanam Havihi API"
    }