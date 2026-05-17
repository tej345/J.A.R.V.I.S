from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)
# Initialize the main FastAPI application instance and pass some basic parameters.
app = FastAPI(
    title="J.A.R.V.I.S. Core API",
    description="The high-performance RAG backend engine.",
    version="1.0.0"
)

# Crucial Security Layer (CORS): This explicitly allows my Next.js frontend 
# running on port 3000 to safely send requests to this Python server on port 8000.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# A tiny test endpoint to check things. 
@app.get("/")
def read_root():
    return {
        "status": "online", 
        "system": "J.A.R.V.I.S. Core Engine Active"
    }