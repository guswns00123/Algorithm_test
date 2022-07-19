import sys

# 큰 사각형에서 작은 사각형을 빼는 문제
# 가장 긴 가로변의 양옆 세로 변의 차이 = 작은 사각형의 세로길이
# 가장 긴 세로변의 양옆 가로 변의 차이 = 작은 사각형의 가로길이

a = []
b = []
w = 0
h = 0
n = int(input())
for i in range(6):
    a = list(map(int,input().split()))
    b.append(a)
for i in range(6):
    if b[i][0] == 1 or b[i][0] == 2:
        if w < b[i][1]:
            w = b[i][1]
            w_idx = i
    elif b[i][0] == 3 or b[i][0] == 4:
        if h < b[i][1]:
            h = b[i][1]
            h_idx = i


small_w = abs(b[(w_idx-1) % 6][1] - b[(w_idx+1) % 6][1])
small_h = abs(b[(h_idx-1) % 6][1] - b[(h_idx+1) % 6][1])

ans = ((w*h) - (small_h * small_w)) * n
print(ans)