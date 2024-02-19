from fastapi import FastAPI
from uuid import UUID

students:dict = {
    # "id":int , 
    "Name":str,
    "Age":int,
    "Sex":str,
    "Height":float
    }

# students_db:list[dict] = []
students_db = {}


app = FastAPI()

@app.get("/")
def home():
    if len(students_db.items()) != 0:
        return students_db.items()
    # else:
    return "Welcome Please create a resource"

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

    # students['id'] = id
    students['Name'] = name
    students['Age'] = age
    students['Sex'] = sex
    students['Height'] = height

    students_db[id] = students
    return {"success": True} 

@app.get("/get_student/{id}")
def get_student(
    id:int
):
    student_id = UUID(int=id)
    if students_db.get(student_id):
        return students_db[student_id]
    return f"Student does not exist at id:{id}"

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
