import sys

def isprime(num):
    n = int(((num)**0.5))
    if num == 1:
        return 0
    elif num == 2:
        return 1
    for i in range(2,n+1):
        if num % i == 0:
            return 0
    return 1

n = int(sys.stdin.readline())

prime = []
for i in range(2,10000):
    if isprime(i) == 1:
        prime.append(i)


for i in range(n):
    m = int(sys.stdin.readline())
    list = []
    for i in prime:
        if i <= m:
            list.append(i)

    for i in list:
        for j in list:
            if i + j == m:
                print(i,j)
                break