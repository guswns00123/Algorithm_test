import sys

n, m = map(int, sys.stdin.readline().split())

set = []
checks = []
for i in range(n+m):
    if i < n:
        set.append(sys.stdin.readline().rstrip()) #rstrip() => 문자열 입력시 개행제거해줌
    else:
        checks.append(sys.stdin.readline().rstrip())


set_dic = {set[i] : i for i in range(len(set))}

c = 0
for i in checks:
    if i in set_dic:
        c += 1

print(c)