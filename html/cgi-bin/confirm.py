#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb
import smtplib
import sys
sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")
import pymysql


cgitb.enable()
form = cgi.FieldStorage()

name = form.getvalue('name')
email  = form.getvalue('email')
confirm=form.getvalue('confirm')

if confirm=="Yes":
    print("""
    <table ALIGN=CENTER BORDER=1 CELLSPACING=1 CELLPADDING=1>
    <tr VALIGN=TOP><td><pre><font size="5">
    Registration Successful
        Thanks!
    <a href="/cgi-bin/regist.py">Register Another.</a>
    <a href="/../regist.html">Back To Home Page</a>
    </font></pre></td></tr></table>""")

    gmail_user = 'wangmaggie1010@gmail.com'  
    gmail_password = 'qqmeiajskemdpsdw'


    #db = pymysql.connect("localhost","root","sweet123","cs531" )
    db=pymysql.connect(host='localhost',
                             user='root',
                             password='sweet123',
                             database='cs531',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor) 

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    #Prepare SQL query to INSERT a record into the database.
    # create_table = """CREATE TABLE STUDENTS (
    # NAME  VARCHAR(30) NOT NULL,
    # EMAIL  VARCHAR(30))"""
    insert_data = "INSERT INTO STUDENTS (NAME, EMAIL) VALUES (%s, %s)"
    val= (name, email)
    try:
    # Execute the SQL command
        cursor.execute(insert_data,val)
    # Commit your changes in the database
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()

    sql="SELECT * FROM STUDENTS WHERE NAME = '%s'" % (name)
    try:
    # Execute the SQL command
        cursor.execute(sql)
        results = cursor.fetchall()
        r=results[len(results)-1]
        name_=r["NAME"]
        email_=r["EMAIL"]

    except:
        print ("Error: unable to fetch data")

    db.close()
    SUBJECT="Registration Success!"
    TEXT="Thank you!"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user,email_, message)
    server.quit()

    

elif confirm=="No":
    print ("""
    <table ALIGN=CENTER BORDER=1 CELLSPACING=1 CELLPADDING=1 >
    <tr VALIGN=TOP><td><pre>
    <font size="5">
    Sorry, The Information Is Incorrect.
        <a href="/cgi-bin/regist.py">Please Register Again</a>
        <a href="/../regist.html">Back To Home Page</a>
    </font></pre></td></tr></table>""")


