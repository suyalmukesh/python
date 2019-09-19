"""A valid mobile number is a ten digit number starting with a 7,8 or 9
"""
import sys
import re
def validate_phone(a):
     format = '[7-9]{1}[0-9]{9}$'
     if re.match(format, a):
         return 'YES'
     else:
         return 'NO'


if __name__ == '__main__':

    input_data = []
    for i in range(int(input())):
        input_data.append(input())


    for i in input_data:
        print(validate_phone(i))
