from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog
from fastapi import HTTPException, status


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        author_id=author_id,
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retreive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def get_all_active_blogs(db: Session):
    return db.query(Blog).filter(Blog.is_active == True).all()


def update_blog_by_id(id: int, blog: UpdateBlog, db: Session, author_id: int = 1):
    blog_object = db.query(Blog).filter(Blog.id == id).first()
    if not blog_object:
        return
    for key, value in blog:
        setattr(blog_object, key, value)
    db.add(blog_object)
    db.commit()
    return blog_object


def delete_blog_by_id(id: int, db: Session):
    blog_object = db.query(Blog).filter(Blog.id == id).first()
    if not blog_object:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Blog with ID not found")

    db.delete(blog_object)
    db.commit()
