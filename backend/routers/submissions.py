from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import api, schemas, models, database

router = APIRouter(prefix="/submissions", tags=["submissions"])


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
