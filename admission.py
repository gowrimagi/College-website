#!C:\python311\python.exe
import cgi
import mysql.connector
print("Content-type:text/html\r\n\r\n")

print("<html>")
print("<body>")

form=cgi.FieldStorage()
fname=form.getvalue("name")
fcourse=form.getvalue("course")
fage=form.getvalue("age")
fgender=form.getvalue("gender")
faddress=form.getvalue("address")
fcontact=form.getvalue("contact")
fmail_id=form.getvalue("mail_id")


mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="Karpagam university"
     )
mycursor=mydb.cursor()

sql="insert into form(name,course,age,gender,address,contact,mail_id)values(%s,%s,%s,%s,%s,%s,%s)";
val=(fname,fcourse,fage,fgender,faddress,fcontact,fmail_id)

mycursor.execute(sql,val)
mydb.commit()

print("<h1>",fname,"</h1>")
print("<h1>",fcourse,"</h1>")
print("<h1>",fage,"</h1>")
print("<h1>",fgender,"</h1>")
print("<h1>",faddress,"</h1>")
print("<h1>",fcontact,"</h1>")
print("<h1>",fmail_id,"</h1>")


print("</body>")
print("</html>")
