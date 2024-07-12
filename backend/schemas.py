from pydantic import BaseModel
from datetime import datetime


class ArticleBase(BaseModel):
    title: str
    url: str


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class SubmissionBase(BaseModel):
    url: str


class SubmissionCreate(SubmissionBase):
    pass


class Submission(SubmissionBase):
    id: int
    upvotes: int
    downvotes: int
    created_at: datetime

    class Config:
        orm_mode = True
