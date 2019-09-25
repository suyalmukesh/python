import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')

print(m.group(0))       # The entire match

print(m.group(1))       # The first parenthesized subgroup.

print(m.group(2))       # The second parenthesized subgroup.

print(m.group(3))       # The third parenthesized subgroup.

print(m.group(1,2,3))   # Multiple arguments give us a tuple.
print ("--------------------------------------------------")
print(m.groups())
print ("--------------------------------------------------")
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict())