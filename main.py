from fastapi import FastAPI
from uuid import UUID
from typing import Optional

students:dict = {
    # "id":int , 
    "Name":str,
    "Age":int,
    "Sex":str,
    "Height":float
    }

students_db = {}


app = FastAPI()

####################### HOME PAGE #######################
@app.get("/")
def home():
    if len(students_db.items()) != 0:
        return students_db.items()
    # else:
    return "Welcome Please create a resource"

####################### CREATE STUDENT RESOURCE #######################
@app.post("/create")
def create_student(
    name:str,
    age:int,
    sex:str,
    height:float
    ):

    id:int = UUID(int=int(len(students_db)+1))
    if (id in students_db.keys()) :
        id:int = UUID(int=int(len(students_db)+2))

    students['Name'] = name
    students['Age'] = age
    students['Sex'] = sex
    students['Height'] = height

    students_db[id] = students
    return {"success": True} 

####################### QUERY STUDENT RESOURCE #######################
@app.get("/get_student/{id}")
def get_student(
    id:int
):
    student_id = UUID(int=id)
    if students_db.get(student_id):
        return students_db[student_id]
    return f"Student does not exist at id:{id}"


####################### UPDATE STUDENT RESOURCE #######################
@app.put("/update_student/")
def update_record(
    id:int,
    name:str,
    age:int,
    sex:str,
    height:float
    ):
    student_id = UUID(int=id)
    if students_db.get(student_id):
        students['Name'] = name
        students['Age'] = age
        students['Sex'] = sex
        students['Height'] = height
        students_db[student_id] = students
        return {f"Record {id} upadated successfully": students}
    else:
        return "Cannot replace an id that does not exist."
    

####################### DELETE RESOURCE #######################

@app.delete("/delete/{id}")
def remove_student(
    id:int
    ):

    del_id = UUID(int=id)
    # if del_id:
    if students_db.get(del_id):
        del students_db[del_id]
        return {f"Sudent id {id} deleted successfully."}
    else:
         return {"invalid student ID"}
