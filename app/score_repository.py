from sqlalchemy import Column, Integer, String, ForeignKey, update
from sqlalchemy.orm import Session, relationship
from .database import Base

from pydantic import BaseModel
from attrs import define

class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    subject = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="score")

class ScoreRequest(BaseModel):
    value: int
    subject: str
    student_id: int

@define
class ScoreSave():
    value: int
    subject: str
    student_id: int

class ScoreRepository():
    def get(self, db: Session, score_id: int) -> Score:
        return db.query(Score).filter(Score.id == score_id).first()

    def save(self, db: Session, score: ScoreSave) -> Score:
        db_score = Score(**score.model_dump())
        db.add(db_score)
        db.commit()
        db.refresh(db_score)
        return db_score
    
    def update(self, db: Session, score_id: int, new_score: ScoreSave) -> Score:
        score = update(Score).where(Score.id == score_id).values(**new_score.model_dump())
        db.execute(score)
        db.commit()
        return score
    
    def delete(self, db: Session, score: Score) -> bool:
        db.delete(score)
        db.commit()
        return True