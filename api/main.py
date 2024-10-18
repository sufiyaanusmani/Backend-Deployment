from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.config import engine
from api.models.models import Base
from api.v1.routes import routes

# Create an instance of the FastAPI class
app = FastAPI()

# Allow origins for CORS
origins = [
    "http://localhost:3000",  # Next.js frontend
    # You can add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(routes.router, prefix="/api/v1")

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
