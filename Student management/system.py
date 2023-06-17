from loginsystem import login,clear
from studlogin import stulogin
from teachlogin import teaclogin

clear()
logindetails = login()

role = logindetails[1]
name = logindetails[0]

if role == 'Student':
    stulogin(name)
elif role == 'Teacher':
    teaclogin(name)
else:
    print('Invalid role!, Please check the "user_pass.txt"')