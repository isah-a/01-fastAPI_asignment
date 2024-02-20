from fastapi import FastAPI, Query, HTTPException
from uuid import uuid4
from typing import List

app = FastAPI()

students_db = {}

####################### HOME PAGE #######################
@app.get("/")
def home():
    if students_db:
        return students_db
    else:
        return "Welcome! Please create a resource."

####################### CREATE STUDENT RESOURCE #######################
@app.post("/create")
def create_student(
    name: str,
    age: int, 
    sex: str, 
    height: float
    ):
    student_id = int(uuid4().int)
    student_data = {"Name": name, "Age": age, "Sex": sex, "Height": height}
    students_db[student_id] = student_data
    return {"success": True, "data": student_data}

####################### QUERY STUDENT RESOURCE #######################
@app.get("/get_student/")
def get_students(
    ids: List[int] = Query(None)
    ):
    studs = []
    for student_id in ids:
        if student_id in students_db:
            studs.append(students_db[student_id])
    return {"data": studs}

####################### UPDATE STUDENT RESOURCE #######################
@app.put("/update_student/{id}")
def update_record(
    id: int, 
    name: str, 
    age: int, 
    sex: str, 
    height: float
    ):
    if id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    student_data = {"Name": name, "Age": age, "Sex": sex, "Height": height}
    students_db[id] = student_data
    return {f"Record {id} updated successfully": student_data}

####################### DELETE RESOURCE #######################
@app.delete("/delete/{id}")
def remove_student(id: int):
    if id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[id]
    return {f"Student id {id} deleted successfully."}
