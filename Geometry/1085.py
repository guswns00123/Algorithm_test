import sys
#직사각형에서 한점의 거리중 최솟값 찾기

x,y,w,h = map(int, sys.stdin.readline().split())
a = abs(x-w)
b = abs(y-h)
c = abs(x)
d = abs(y)

if a < b and a < c and a < d:
    print(a)
elif b < a and b < c and b < d:
    print(b)
elif c < a and c < b and c < d:
    print(c)
else:
    print(d)
