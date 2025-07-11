from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, default='todo') # todo / in-progress / done
    is_archived = Column(Boolean, default=False)