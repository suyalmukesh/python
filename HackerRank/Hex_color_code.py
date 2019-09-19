import sys
import re
if __name__ == '__main__':
    input_css = []
    for i in range(int(input())):
        input_css.append(input())

    open = 0
    lst = []
    left, right, pattern2 = '[\b{\w]', '}', '[#]\w+'
    pattern = r'#[a-fA-F0-9]{3,6}'  # correct

    for i in input_css:
        temp = []
        if '{' in i:
            open = 1
            continue
        else:
            if '}' in i:
             open = 0
             continue

        if open == 1:
             a = re.findall(pattern,i)
             for i in a:
                 lst.append(i)

    for i in lst:
        print(i)








