#!/usr/bin/env python

import api, schemas, models, database
# from eliot import log_call, to_file
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# to_file(sys.stdout)
# to_file(open("/tmp/get_secrets.log", "w"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static",
          StaticFiles(directory="frontend/public"),
          name="static")


@app.get("/")
async def read_index():
    return FileResponse("frontend/public/index.html")


router = APIRouter()


@router.get("/articles", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    articles = api.get_articles(db, skip=skip, limit=limit)
    return articles


@router.post("/articles", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(database.get_db)):
    return api.create_article(db, article)


@router.get("/submissions", response_model=list[schemas.Submission])
def read_submissions(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    submissions = api.get_submissions(db, skip=skip, limit=limit)
    return submissions


@router.post("/submissions", response_model=schemas.Submission)
def create_submission(submission: schemas.SubmissionCreate, db: Session = Depends(database.get_db)):
    return api.create_submission(db, submission)


@router.put("/submissions/{submission_id}", response_model=schemas.Submission)
def update_submission_votes(submission_id: int, upvotes: int, downvotes: int, db: Session = Depends(database.get_db)):
    return api.update_submission_votes(db, submission_id, upvotes, downvotes)


@router.get("/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    articles = api.get_articles(db, skip=skip, limit=limit)
    return articles


@router.post("/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(database.get_db)):
    return api.create_article(db, article)


@router.get("/", response_model=list[schemas.Submission])
def read_submissions(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    submissions = api.get_submissions(db, skip=skip, limit=limit)
    return submissions


@router.post("/", response_model=schemas.Submission)
def create_submission(submission: schemas.SubmissionCreate, db: Session = Depends(database.get_db)):
    return api.create_submission(db, submission)


@router.put("/{submission_id}", response_model=schemas.Submission)
def update_submission_votes(submission_id: int, upvotes: int, downvotes: int, db: Session = Depends(database.get_db)):
    return api.update_submission_votes(db, submission_id, upvotes, downvotes)


app.include_router(router)
