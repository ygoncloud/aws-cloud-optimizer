from fastapi import FastApi

app = FastAPI(
        title="Alibaba Cloud Cost Optimization API",
        description="Automated detection and decommissioning of unused Alibaba Cloud Resources",
        version="1.0.0",
)

from app import scanner, decommission

@app.get("/")
def root():
    return {"message": "Cloud Cost Optimization API is running!"}
