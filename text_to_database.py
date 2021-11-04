import sqlite3

file1 = open("student.txt","r")
data = file1.readlines()
file1.close()

con = sqlite3.connect("student_info.db")
for row in data:
    query = "insert into stud_info values('"+row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"')"
    con.execute(query)
    con.commit()
con.close()




