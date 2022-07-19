import sys


x, y = map(int,input().split())
w, z = map(int,input().split())
a, b = map(int,input().split())

if x != w and x != a:
    c = x
else:
    if x == a:
        c = w
    else:
        c = a
if y != z and y != b:
    d = y
else:
    if y == b:
        d = z
    else:
        d = b

print(c, d)



