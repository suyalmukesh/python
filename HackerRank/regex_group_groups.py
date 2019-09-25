import re

m = re.findall(r"([A-Za-z0-9])\1+",input())
if len(m) == 0:
    print(-1)
else:
    print(m[0])