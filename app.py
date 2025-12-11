from flask import Flask, render_template, request 
import mysql.connector 
app = Flask(__name__) 
# MySQL Connection 
db = mysql.connector.connect( 
host="localhost", 
user="root", 
password="2004",  # <-- Replace with your MySQL password 
database="student_demo" 
) 
cursor = db.cursor() 
@app.route("/") 
def form(): 
    return render_template("form.html") 
@app.route("/submit", methods=["POST"]) 
def submit(): 
    name = request.form["name"] 
    email = request.form["email"] 
    query = "INSERT INTO users (name, email) VALUES (%s, %s)" 
    values = (name, email) 
    cursor.execute(query, values) 
    db.commit() 
    return f""" 
    <h2>Data Saved Successfully!</h2> 
    <p><b>Name:</b> {name}</p> 
    <p><b>Email:</b> {email}</p> 
    <a href="/">Go Back</a> 
    """ 
if __name__ == "__main__":
    app.run(debug=True)