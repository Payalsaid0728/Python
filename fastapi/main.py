import mysql.connector
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI(
    title="Student API",
    description="Simple Student Management REST API",
    version="1.0"
)

#Connect to MySQL
dbConnection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="payal"
)

print ("MySQL Connected Successfully")

dbCommand=dbConnection.cursor(dictionary=True)


class Student(BaseModel):
    RollNo: int
    Name: str
    Course: str
    Age: int
    Email_Id: str
    Department: str


class StudentUpdate(BaseModel):
    RollNo:int
    Name:str



@app.get("/api/get_all_student")
def get_all_student():
    dbCommand.execute("SELECT * FROM student")
    student=dbCommand.fetchall()
    
    return student


@app.post("/api/student")
def add_students(student:Student):

    query="INSERT INTO student(RollNo,Name,Course,Age,Email_id,Department) values(%s,%s,%s,%s,%s,%s)"

    values=(
        student.RollNo,
        student.Name,
        student.Course,
        student.Age,
        student.Email_Id,
        student.Department
    )

    dbCommand.execute(query,values)
    dbConnection.commit()

    return{
        "message":"student added successfully"
    }


@app.put("/api/student")
def update_student(student:StudentUpdate):

    query="UPDATE student SET Name=%s WHERE RollNo=%s"

    values=(
        student.Name,
        student.RollNo
    )

    dbCommand.execute(query,values)
    dbConnection.commit()

    return{
        "message":"Student details updated successfully"
    }


@app.delete("/api/student/{RollNo}")
def delete_student(RollNo:int):

    query="DELETE FROM student WHERE RollNo=%s"

    values=(RollNo,)

    dbCommand.execute(query,values)
    dbConnection.commit()

    return{
        "message":"student deleted successfully"
    }
