from typing import List
from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId

class BlogPostCreate(BaseModel):
    title: str
    short_description: str
    description: str
    tags: List[str]
    created_at: str = str(datetime.now().isoformat())  
    updated_at: str = str(datetime.now().isoformat()) 

class BlogPostResponse(BaseModel):
    title: str
    short_description: str
    description: str
    tags: List[str]
    created_at: str = str(datetime.now().isoformat())  
    updated_at: str = str(datetime.now().isoformat())
    id: str
