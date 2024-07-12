import models, schemas
from sqlalchemy.orm import Session


def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Article).offset(skip).limit(limit).all()


def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(title=article.title, url=article.url)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_submissions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Submission).offset(skip).limit(limit).all()


def create_submission(db: Session, submission: schemas.SubmissionCreate):
    db_submission = models.Submission(url=submission.url)
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission


def update_submission_votes(db: Session, submission_id: int, upvotes: int, downvotes: int):
    db_submission = db.query(models.Submission).filter(models.Submission.id == submission_id).first()
    if db_submission:
        db_submission.upvotes = upvotes
        db_submission.downvotes = downvotes
        db.commit()
        db.refresh(db_submission)
    return db_submission
