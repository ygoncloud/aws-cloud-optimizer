from fastapi import FastApi

app = FastAPI(
        title="Azure Cloud Cost Optimization API",
        description="Automated detection and decommissioning of unused Azure Cloud Resources",
        version="1.0.0",
)

from app import scanner, decommission

@app.get("/")
def root():
    return {"message": "Cloud Cost Optimization API is running!"}
