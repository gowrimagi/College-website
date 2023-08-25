#!C:\python311\python.exe
import cgi
import mysql.connector
print("content-type:text/html\r\n\r\n")

print("<html>")
print("<body>")

form=cgi.FieldStorage()
froll=form.getvalue("roll_no")
fpass=form.getvalue("password")

print(froll,fpass)

mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="karpagam university"
     )
mycursor=mydb.cursor()

sql="insert into user (Roll_no,password)values(%s,%s)";
val=(froll,fpass)

mycursor.execute(sql,val)
mydb.commit()

print("<h1>",froll,fpass,"</hi>")
print("</body>")
print("</html>")