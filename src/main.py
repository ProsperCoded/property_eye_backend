"""
Property Eye Fraud Detection POC - Main Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Property Eye Fraud Detection API",
    description="POC system for detecting property fraud by comparing agency listings against UK Land Registry data",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS for future frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - API health check"""
    return {
        "status": "ok",
        "message": "Property Eye Fraud Detection API",
        "version": "0.1.0",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "fraud-detection-api"}


@app.on_event("startup")
async def startup_event():
    """Initialize resources on application startup"""
    # TODO: Initialize database connection
    # TODO: Verify PPD volume path exists
    pass


@app.on_event("shutdown")
async def shutdown_event():
    """Clean up resources on application shutdown"""
    # TODO: Close database connection
    pass
