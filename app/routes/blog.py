
from fastapi import APIRouter, HTTPException
from typing import List
from app.models import BlogPostCreate, BlogPostResponse
from app.database import db
from datetime import datetime 
from bson import ObjectId

router = APIRouter()


@router.post("/", response_model=BlogPostResponse)

async def create_post(post_data: BlogPostCreate):

    current_time = datetime.now().isoformat()

    post_data.created_at = str(current_time)
    post_data.updated_at = str(current_time)


    inserted_post = await db.db["blog_posts"].insert_one(post_data.model_dump())

    post_id = str(inserted_post.inserted_id)
    

    created_post = {
        **post_data.model_dump(),
        "created_at": str(current_time),  
        "updated_at": str(current_time),  
        "_id": post_id
    }
    return created_post


@router.get("/", response_model=List[BlogPostResponse])
async def get_posts():

    blog_posts_cursor = db.db["blog_posts"].find()
    blog_posts = [BlogPostResponse(id=str(post["_id"]), **post) async for post in blog_posts_cursor]
    return blog_posts


@router.get("/{post_id}", response_model=BlogPostResponse)
async def get_post(post_id: str):

    post = await db.db["blog_posts"].find_one({"_id": ObjectId(post_id)})
    print(post)
    if post:
        return BlogPostResponse(id=str(post["_id"]), **post)
    else:
        raise HTTPException(status_code=404, detail="Blog gönderisi bulunamadı")


@router.put("/{post_id}", response_model=BlogPostResponse)
async def update_post(post_id: str, post_data: BlogPostCreate):

    existing_post = await db.db["blog_posts"].find_one({"_id": ObjectId(post_id)})
    
    if existing_post:

        created_at = existing_post.get("created_at")

        updated_at = str(datetime.now().isoformat())
        

        updated_post = {
            **post_data.model_dump(),
            "created_at": created_at,
            "updated_at": updated_at
        }
        await db.db["blog_posts"].update_one({"_id": ObjectId(post_id)}, {"$set": updated_post})
        

        return BlogPostResponse(id=str(post_id), **updated_post)
    else:
        raise HTTPException(status_code=404, detail="Blog gönderisi bulunamadı")


@router.delete("/{post_id}", response_model=BlogPostResponse)
async def delete_post(post_id: str):

    deleted_post = await db.db["blog_posts"].find_one_and_delete({"_id": ObjectId(post_id)})
    if deleted_post:
        return BlogPostResponse(id=str(post_id), **deleted_post)
    else:
        raise HTTPException(status_code=404, detail="Blog gönderisi bulunamadı")
