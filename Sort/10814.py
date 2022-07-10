import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
    l.append(sys.stdin.readline().split())

for i in l : i[0] = int(i[0])
#나이는 정수이므로 모두 int로 바꿔준다

l.sort(key = lambda x: x[0] )

for i in range(n):
    print(*l[i])
