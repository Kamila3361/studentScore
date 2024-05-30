# studentScore
Запуск проекта: 
uvicorn app.main:app --reload

Документация

POST /students/ -
    
    Request body (required):
    {
        "first_name": "string",
        "second_name": "string",
        "school": "string",
        "grade_number": 11,
        "grade_letter": "s"
    }

    Response body
    {
        "first_name": "Marat",
        "second_name": "Duman",
        "grade_number": 5,
        "id": 4,
        "school": "Astana",
        "grade_letter": "A"
    }

GET /students/{student_id} - 
    
    No need request body

    Successful Response body
    {
        "first_name": "Kamila",
        "second_name": "Tashimova",
        "grade_number": 11,
        "id": 1,
        "school": "Sh.Smagoluv",
        "grade_letter": "B"
    }

PATCH /students/{student_id} - 
    
    Request body(required):
    {
        "first_name": "string",
        "second_name": "string",
        "school": "string",
        "grade_number": 11,
        "grade_letter": "s"
    }

    Successful Response:  changed

DELETE /students/{student_id} - 

    No need request body

    Successful Response:  deleted

POST /score/ -
    
    Request body (required):
    {
        "value": 0,
        "subject": "string",
        "student_id": 0
    }

    Response body
    {
        "value": 5,
        "subject": "Phys",
        "student_id": 3,
        "id": 4
    }

GET /score/{score_id} - 
    
    No need request body

    Successful Response body
    {
        "value": 4,
        "subject": "Kaz",
        "student_id": 1,
        "id": 2
    }

PATCH /score/{score_id} - 
    
    Request body(required):
    {
        "value": 0,
        "subject": "string",
        "student_id": 0
    }

    Successful Response:  changed

DELETE /score/{score_id} - 

    No need request body

    Successful Response:  deleted
