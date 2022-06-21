import sys
import math
#소수
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# def isprime(num):
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     for i in range(2,num):
#         if num % i == 0:
#             return 0
#     return 1

def findprime(i):
        if (i == 1) : return 0
        elif (i == 2 or i == 3): 
            return 1 
        elif (i % 2 == 0) : return 0
        else:
            div = 3
            while (i > div):
                if (i % div == 0) : 
                    return 0
                div += 2
            return 1

res = 0
min = m+1
for i in range(n,m+1):
    if findprime(i) == 1:
        res += i
        if min > i:
            min = i

if res == 0:
    print(-1)
else:
    print(res)
    print(min)
