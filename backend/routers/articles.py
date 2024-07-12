from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import api, schemas, models, database

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    articles = api.get_articles(db, skip=skip, limit=limit)
    return articles


@router.post("/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(database.get_db)):
    return api.create_article(db, article)
