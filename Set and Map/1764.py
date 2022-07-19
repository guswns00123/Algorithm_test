import sys

n, m = map(int, sys.stdin.readline().split())

l1= []
l2= []
for i in range(n+m):
    if i <n :
        l1.append(sys.stdin.readline().rstrip())
    else:
        l2.append(sys.stdin.readline().rstrip())


l1_set = set(l1)
l2_set = set(l2)

res = list(l1_set & l2_set)
res.sort()
print(len(res))
for i in res:
    print(i)