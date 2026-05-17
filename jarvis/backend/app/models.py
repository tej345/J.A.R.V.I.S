from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

# this python class represents a table inside postgre
class ToDoTask(Base):
    __tablename__ = "todo_tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default =False)
