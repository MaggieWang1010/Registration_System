#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
print("""
<html>
<center><head><title>Registration Form</title></head><body>
<font color="red" size="7">Registration Form</font>

<form action="/cgi-bin/process.py" method=GET>
<table align=center datasrc="#xmlRegData" border=2>

<tr><td><font color="black" size="5">Name:</font></td>
<td><input type=text name=name value="" size=30></td></tr>
<tr><td><font color="black" size="5">Email:</font></td>
<td><input type=text name=email value="" size=30></td></tr>
</table>
    <input type=submit value=Submit name=B1>        
    <input type=reset value=Reset name=B2>
</form>
</body>
</center>
</html>""")

