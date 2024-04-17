from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from db.repository.blog import create_new_blog, retreive_blog, get_all_active_blogs, update_blog_by_id, \
    delete_blog_by_id

router = APIRouter()


@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(
        blog=blog, db=db, author_id=1)
    return blog


@router.get("/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this ID not found")
    return blog


@router.get("/", response_model=list[ShowBlog])
def get_blogs(db: Session = Depends(get_db)):
    return get_all_active_blogs(db=db)


@router.put("/{id}", response_model=ShowBlog)
def update_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    blog = update_blog_by_id(id=id, blog=blog, db=db, author_id=1)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID doesn't exist")
    return blog


@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    return delete_blog_by_id(id, db)
