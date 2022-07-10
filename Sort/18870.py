import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))
res = sorted(list(set(li)))

dic = {res[i] : i for i in range(len(res))}
for i in li:
    print(dic[i], end = ' ')

