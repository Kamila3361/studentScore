from fastapi import FastAPI, Response, Depends, HTTPException

from .student_repository import StudentRequest, StudentRepository
from .score_repository import ScoreRepository, ScoreRequest

from sqlalchemy.orm import Session
from .database import SessionLocal, Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

students = StudentRepository()
scores = ScoreRepository()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/")
def post_student(student: StudentRequest, db: Session=Depends(get_db)):
    student = students.save(db, student)
    return student

@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session=Depends(get_db)):
    student = students.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Not Found")
    return student

@app.patch("/students/{student_id}")
def patch_student(student_id: int, new_student: StudentRequest, db: Session=Depends(get_db)):
    student = students.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Not Found")
    students.update(db, student_id, new_student)
    return Response(content="changed", status_code=200)

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session=Depends(get_db)):
    student = students.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Not Found")
    students.delete(db, student)
    return Response(content="Deleted", status_code=200)

@app.post("/score/")
def post_student(score: ScoreRequest, db: Session=Depends(get_db)):
    student_id = score.student_id
    student = students.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student Not Found")
    saved_score = scores.save(db, score)
    return saved_score

@app.get("/score/{score_id}")
def get_student(score_id: int, db: Session=Depends(get_db)):
    score = scores.get(db, score_id)
    if not score:
        raise HTTPException(status_code=404, detail="Not Found")
    return score

@app.patch("/score/{score_id}")
def patch_student(score_id: int, new_score: ScoreRequest, db: Session=Depends(get_db)):
    student_id = new_score.student_id
    student = students.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student Not Found")
    
    score = scores.get(db, score_id)
    if not score:
        raise HTTPException(status_code=404, detail="Not Found")
    
    scores.update(db, score_id, new_score)
    return Response(content="changed", status_code=200)

@app.delete("/score/{score_id}")
def delete_student(score_id: int, db: Session=Depends(get_db)):
    score = scores.get(db, score_id)
    if not score:
        raise HTTPException(status_code=404, detail="Not Found")
    scores.delete(db, score)
    return Response(content="Deleted", status_code=200)
