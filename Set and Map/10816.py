import sys

n = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

checks = list(map(int, sys.stdin.readline().split()))

dic = dict()
# 숫자 카드와 개수를 딕셔너리에 담기
for i in cards:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

for i in checks:
    if i in dic:
        print(dic[i], end = " ")
    else:
        print(0, end = " ")
            # print(cards_list)
            # print(i)
        
