import sys

#소수 찾기
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
# 1< n <= 123456
# n의 범위가 제한적이므로 미리 소수를 다 찾아놓는다
prime = []
for i in range(2,246912):
    if isprime(i) == 1:
        prime.append(i)

n = int(sys.stdin.readline())
list = []
while True:
    if n == 0 : break
    c = 0
    for i in prime:
        if n < i <= 2*n:
            c+=1
        # if i in prime:
        #     c+=1
        # 이렇게 실행 시 시간이 더걸림
        # 왜그럴까나..
    print(c)
    n = int(sys.stdin.readline())

