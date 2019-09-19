import re
"""
Valid email addresses must follow these rules:
    It must have the username@websitename.extension format type.
    The  username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits. <done>
    The maximum length of the extension is 3. <done>
"""

def validate(a,valid):
    format = '[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    if re.match(format,a):
       valid.append(a)

if __name__ == '__main__':
    inp, valid = [], []

    for i in range(int(input())):
        inp.append(input())

    for i in (inp):
        validate(i,valid)
    print(valid)



