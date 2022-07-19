import sys
# list의 경우 소요시간이 길어 이 문제의 경우 dictionary 알고리즘을 이용하여 풀어야 시간내에 풀수 있었다.
# https://wayhome25.github.io/python/2017/06/14/time-complexity/
# list 와 dic 의 operation에 따른 Big-O 가 명시 되어있어서 보고 참조하면 된다.

n = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))
cards_list = {cards[i] : i for i in range(len(cards))}
#cards 를 리스트로 바꾸고 dict으로 바꾸는 방법
m = int(sys.stdin.readline())

checks = list(map(int, sys.stdin.readline().split()))
dic = {checks[i] : i for i in range(len(checks))}
res = []
for i in dic.keys():
        if i in cards_list:
            cards_list.pop(i) #O(1)
            res.append(1) #O(1)
            # print(cards_list)
            # print(i)
        else:
            res.append(0)

print(*res)