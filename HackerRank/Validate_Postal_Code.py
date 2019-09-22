import re
import sys
def validate_postal_code(n):
    # range 100000 to 999999
    #regex_integer_in_range = '[1-9][0-9][0-9][0-9][0-9][0-9]$'
    regex_integer_in_range = '[1-9][0-9]{5}$'
    regex_alternating_repetitive_digit_pair = '(\d)(?=\d\1)'
   #  1 3   3 5   2 4    4  6

    # 212187

    if re.match(regex_alternating_repetitive_digit_pair, n):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':

    n = input()
    validate_postal_code(n)

