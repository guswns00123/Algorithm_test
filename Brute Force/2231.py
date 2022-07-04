
import sys
import math
#분해 합
# 245의 분해합은 256(245 + 2 + 4 + 5)
# 245는 256의 생성자가 된다.
# 생성자는 여러 개인 자연수일수도 있다 그중 가장 작은 생성자를 구해라

n = int(sys.stdin.readline())
k = 1 #k를 1부터 체크해야댐
# 
flag = 0
# print(m,k)
while True:
    if k < 0:
        break
    ans = k + sum(map(int, str(k))) #각자리수의 합
    if k >= n : 
        break
    if ans == n:
        flag = 1
        print(k)
        break
    else:
        k+=1
if flag == 0:
    print(0)