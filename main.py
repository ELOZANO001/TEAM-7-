# Esteban Lozano, David Li, Jacob Logid, James Meyko
# 12/9/2023
# Program 1: GROUP PROJECT

import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS student")

cursor.execute(
    "CREATE TABLE student(student_id text PRIMARY KEY, first_name text, last_name text, email text, date_of_birth text, age integer, grade_level text)")
student_info = [
    ("W1001", "Joel", "Embid", "joel99@gmail.com", "12/11/2001", 22, "Senior"),
    ("W1002", "Mike", "Jones", "mike24@gmail.com", "06/24/2003", 20, "Sophomore"),
    ("W1003", "Anthony", "Edwards", "anthony5@gmail.com", "01/15/2003", 20, "Sophomore"),
    ("W1004", "Dustin", "Johnson", "dustin0523@gmail.com", "05/23/2002", 21, "Junior"),
    ("W1005", "Rory", "Mcllroy", "rory2005@gmail.com", "06/18/2001", 22, "Senior"),
    ("W1006", "Jon", "Rahm", "jon600@gmail.com", "11/23/2002", 21, "Junior"),
    ("W1007", "Adam", "Ondra", "adam17@gmail.com", "01/01/2001", 22, "Senior"),
    ("W1008", "Brandon", "Sandau", "Branden1239@gmail.com", "01/01/2001", 22, "Freshman"),
    ("W1009", "Sandy", "Deso", "Sandy_eyes@gmail.com", "01/01/1003", 20, "Junior"),
    ("W1010", "Joe", "Bama", "Joe4thewin@gmail.com", "01/01/2004", 19, "Senior"),
]

cursor.executemany("INSERT INTO student VALUES(?,?,?,?,?,?,?)", student_info)

def display_student_info():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    
# Print database rows
print("\n*********STUDENT INFO****************")
for row in cursor.execute("SELECT * FROM student"):
    print(row)

connection.close()

if __name__ =="__main__":
    display_student_info()



