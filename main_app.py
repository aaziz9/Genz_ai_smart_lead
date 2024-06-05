from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.account_controller import v1_account_router

app = FastAPI(
    title="GenZ Co-Pilot Plugin API",
    description="Allows co-pilot to fetch ",
    version="1.0.0",
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "GenZ Co-pilot Plugin API that can response with lead account information"
        },
    ]
)

# Add the CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Routers
app.include_router(v1_account_router, prefix="/api/v1/accounts")
