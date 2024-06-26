from fastapi import APIRouter
from fastapi import Request, Depends
from sqlalchemy.orm import Session
from db.repository.blog import get_all_active_blogs, retreive_blog
from db.session import get_db
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def home(request: Request, alert: str | None = None, db: Session = Depends(get_db)):
    blogs = get_all_active_blogs(db=db)
    context = {"request": request, "blogs": blogs, "alert": alert}
    return templates.TemplateResponse("blogs/home.html", context=context)


@router.get("/app/blog/{id}")
def blog_detail(request: Request, id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id, db)
    return templates.TemplateResponse("blogs/detail.html", {"request": request, "blog": blog})
