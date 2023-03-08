#!C:\Python310\python.exe
print("Content-type:text/html\r\n\r\n")

import random
#Andile Ngwenya and Tyrone Sutherland-Macleod
num1=random.randint(1,1000)
num2=random.randint(1,1000)

if num1==num2:
    num2=num2-1

    
print("<html>")
print("<head></head>")
print("<body>")
print("<p>Pick larger number</p>")
if num1>num2:
    print("<p><a href='win.py'>")
    print(num1)
    print("</a></p>")
    print("<p><a href='lose.py'>")
    print(num2)
    print("</a></p>")
else:
    print("<p><a href='lose.py'>")
    print(num1)
    print("</a></p>")
    print("<p><a href='win.py'>")
    print(num2)
    print("</a></p>")
print("</body>")
print("</html>")
