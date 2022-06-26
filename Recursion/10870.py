import sys
#파보나치 수
n = int(sys.stdin.readline())

def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(n))