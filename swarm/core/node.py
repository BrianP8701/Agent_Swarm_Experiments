from pydantic import BaseModel
from typing import Optional, List
from settings import Settings

settings = Settings() # For config paths

class Node(BaseModel):
    id: int
    type: str
    data: dict
    parent: Optional['Node'] = None
    children: List['Node'] = []
    output: Optional[dict] = None

    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True
        populate_by_name = True
        
    def jsonify(self):
        return {
            "id": self.id,
            "task_type": self.type,
            "parent_id": self.parent.id if self.parent is not None else None,
            "children_ids": [child.id for child in self.children],
            "input_data": self.data,
            "output_data": self.output
        }