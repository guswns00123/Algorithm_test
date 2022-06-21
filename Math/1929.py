import sys

#같은 소수 찾기지만
# n의 범위를 제곱근 까지 줄여서 시간 대폭 줄일수 있음.

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


n, m = map(int, sys.stdin.readline().split())
list = []
for i in range(n,m+1):
    if isprime(i) == 1:
        print(i)

