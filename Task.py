from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    """
    Represents a task with scheduling metadata.
    """
    task_id: int
    priority: int  # Higher value = higher priority
    arrival_time: datetime
    deadline: datetime
    description: str = ""
    
    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority}, desc='{self.description}')"
