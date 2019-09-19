"""2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
"""
import sys
import email.utils
import re
# -----------------------------------------------------------------
def fun(s):
    # return True if s is a valid email, else return False
    format = '[^-._][a-zA-Z.0-9_-]+@[^0-9][a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    if re.match(format, s):
        return True
# -----------------------------------------------------------------
def validate(a):
    a,b = email.utils.parseaddr(a)
    if(fun(b)):
        print(email.utils.formataddr((a,b)))
# -----------------------------------------------------------------
if __name__ == '__main__':
 my_input = []
 for i in range(int(input())):
     my_input.append(input())

 for i in my_input:
     validate(i)