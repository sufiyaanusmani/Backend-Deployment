from fastapi import FastAPI

from api.core.config import engine
from api.models.models import Base

# Create an instance of the FastAPI class
app = FastAPI()


# Create tables
@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)

# Define a route for the root URL ("/")
@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}

# Run the application using 'uvicorn' if this script is run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) # uvicorn api.main:app --reload
