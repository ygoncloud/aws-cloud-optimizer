from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, Base, engine
from app.models import CloudResource
from app.scanner import scan_resources
from app.decommission import decommission_resources

app = FastAPI(
        title="Azure Cloud Cost Optimization API",
        description="Automated detection and decommissioning of unused Azure Cloud Resources",
        version="1.0.0",
        )

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Cloud Cost Optimization API is running!"}

@app.get("/resources/unused")
def get_unused_resources(db: Session = Depends(get_db)):
    return db.query(CloudResource).filter(CloudResource.status == "unused").all()

@app.get("/savings")
def get_savings(db: Session = Depends(get_db)):
    unused_resources = db.query(CloudResource).filter(CloudResource.status == "unused").all()
    total_savings = sum([r.cost_savings for r in unused_resources])
    return {"estimated_savings": f"${total_savings:.2f} per year"}

@app.post{"/scan"}
def scan_cloud_resources(db: Session = Depends(get_db)):
    unused_resources = scan_resources()
    for res in unused_resources:
        db.add(CloudResource(**res))
    db.commit()
    return {"message": f"{len(unused_resources)} unused resources added to DB."}

@app.post("/decommission")
def decommission_cloud_resources():
    result = decommission_resources()
    return result
