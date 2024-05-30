from sqlalchemy import Column, Integer, String, update
from sqlalchemy.orm import Session, relationship
from .database import Base

from pydantic import BaseModel, conint, Field
from attrs import define

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    second_name = Column(String, index=True)
    school = Column(String)
    grade_number = Column(Integer)
    grade_letter = Column(String(1))

    score = relationship("Score", back_populates="student")

class StudentRequest(BaseModel):
    first_name: str
    second_name: str
    school: str
    grade_number: conint(ge=0, le=11)  
    grade_letter: str = Field(..., max_length=1)

@define
class StudentSave():
    first_name: str
    second_name: str
    school: str
    grade_number: int
    grade_letter: str

class StudentRepository():
    def get(self, db: Session, student_id: int) -> Student:
        return db.query(Student).filter(Student.id == student_id).first()

    def save(self, db: Session, student: StudentSave) -> Student:
        db_student = Student(**student.model_dump())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    
    def update(self, db: Session, student_id: int, new_student: StudentSave) -> Student:
        student = update(Student).where(Student.id == student_id).values(**new_student.model_dump())
        db.execute(student)
        db.commit()
        return student
    
    def delete(self, db: Session, student: Student) -> bool:
        db.delete(student)
        db.commit()
        return True