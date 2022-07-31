#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()
confirm=form.getvalue('confirm')

if confirm=="Yes":
    print("""
    <table ALIGN=CENTER BORDER=1 CELLSPACING=1 CELLPADDING=1>
    <tr VALIGN=TOP><td><pre><font size="5">
    Registration Successful
        Thanks!
    <a href="/cgi-bin/regist.py">Register Another.</a>
    <a href="/cgi-bin/home.py">Back To Home Page</a>
    </font></pre></td></tr></table>""")

elif confirm=="No":
    print ("""
    <table ALIGN=CENTER BORDER=1 CELLSPACING=1 CELLPADDING=1 >
    <tr VALIGN=TOP><td><pre>
    <font size="5">
    So, The Information Is Incorrect.
        <a href="/cgi-bin/regist.py">Please Register Again</a>
        <a href="/cgi-bin/home.py">Back To Home Page</a>
    </font></pre></td></tr></table>""")

