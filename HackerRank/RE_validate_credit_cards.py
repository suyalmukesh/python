"""
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456


  It must start with a 4,5  or 6 .
  '[456][0-9]-[0-9]{4}-[0-9]{4}-[0-9]{4}'
► It must contain exactly 16  digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits."""

import re
import sys

def validate_credit_card(a):
     TESTER = re.compile(
        r"^"
        r"(?!.*(\d)(-?\1){3})"
        r"[456]\d{3}"
        r"(\d{12}|(-\d{4}){3})"
        r"$")

     re1 = '[456]{1}[0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}'  # with hyphen
     re11 = '[456]{1}[0-9]{3}[0-9]{4}[0-9]{4}[0-9]{4}'  # without hyphen
     re2 =  '(.)\1{3}'
     if (re.match(TESTER,a)):
         print("Valid")
     else:
         print("Invalid")


if __name__ == '__main__':
    in_list = []
    for i in range(int(input())):
        in_list.append(input())

    for i in in_list:
        validate_credit_card(i)


