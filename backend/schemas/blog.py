from pydantic import BaseModel, root_validator
from datetime import datetime


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: str | None = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
            return values


class ShowBlog(BaseModel):
    title: str
    content: str | None
    created_at: datetime
    is_active: bool

    class Config():
        orm_mode = True


class UpdateBlog(CreateBlog):
    is_active: bool = False
