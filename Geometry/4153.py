import sys

res = []
while True:
    res = list(map(int,input().split()))
    res.sort()
    if res[0] == 0 and res[1] ==0 and res[2] == 0 :
        break
    if res[0]**2 + res[1]**2 == res[2]**2:
        print("right")
    else: print("wrong")

