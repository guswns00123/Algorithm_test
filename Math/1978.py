import sys
#소수 찾기
#에라토스테네스의 체
#소수 2 부터 n이 나눠지면 거르고
#그다음 3,5,7... 이런식으로 계속 루트돌리기
a = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
c = 0
f = 0
for i in list:
    if (i <= 1) : continue
    elif (i == 2 or i == 3): 
        c += 1 
        # print(i)
    elif (i % 2 == 0) : continue
    else:
        f = 0
        div = 3
        while (i > div):
            if (i % div == 0) : 
                f = 1
                # print(i)
                break
            div += 2
        if f == 0: 
            # print(i)
            c += 1
        else: continue

print(c)

    