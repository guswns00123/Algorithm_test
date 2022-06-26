import sys
#팩토리얼

n = int(sys.stdin.readline())

def fac(n):
    if n == 1 : return 1
    elif n == 0 : return 1
    else:
        return n * fac(n-1)

print(fac(n))