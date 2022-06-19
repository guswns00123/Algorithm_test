import sys
#delivery sugar

# N킬로 그램 설탕 배달
# 3kg , 5kg 봉지가 존재
# 18kg 배달 시 더 적은 봉지 선호
# 5kg 3개 와 3kg 1개
a = int(sys.stdin.readline())

bag = 0
while a >= 0:
    if a % 5 == 0:
        bag += (a // 5)
        print(bag)
        break
    a -= 3
    bag += 1
else :
    print (-1)