from sqlalchemy import Column, Integer, String
from app.database import Base

class CloudResource(Base):
    __tablename__ = "cloud_resources"
    id = Column(Integer, primary_key=True, index=True)
    resource_id = Column(String, unique=True, index=True)
    name = Column(String)
    type = Column(String)
    status = Column(String)
    cost_saving = Column(Integer)

