import sys

# 블랙잭 게임
# N장의 카드중 3장을 골라 숫자 M의 넘지 않으며 가깝게 만들기

n, m = map(int, sys.stdin.readline().split())

l = []
l = list(map(int,sys.stdin.readline().split())) #N장의 카드를 한줄에 입력해서 list화


max = 0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        for k in range(len(l)):
            if k == i or k == j: #이미 뽑은 카드인경우 스킵
                continue
            elif l[i] + l[j] + l[k] > m: # m보다 크면 스킵
                continue
            else:
                sum = l[i] + l[j] + l[k]
                if sum <= m : # sum이 m 보다 작거나 같으면 체크
                    if sum >= max : #max값보다 그값이 크면 저장
                        max = sum
    
        if j + 1 == len(l): break



print(max)