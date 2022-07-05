import sys

#체스판 다시 칠하기


# M * N 크기의 보드를 8 * 8 크기의 체스판으로 만들것
# 변을 공유하는 두개의 사각형은 다른 색으로 칠해져 있어야한다
# 하나는 맨 왼쪽 위칸이 흰색 다른 하나는 검은색
# 보드판을 잘랐을 때 몇개의 정사각형을 다시 칠 해야하는지 구하시오.

n, m = map(int,sys.stdin.readline().split())
l = []
for i in range(n):
    l.append(input())

count = []

for i in range(n-7):
    for j in range(m-7):
        idx1 = 0
        idx2 = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a + b) % 2 == 0: #(0,0), (0,2) 같은 짝수 판때기일때
                    if l[a][b] != 'W':
                        idx1 += 1
                    if l[a][b] != 'B':
                        idx2 += 1

                else: #(1,0), (1,2) 홀수 판때기 일때
                    if l[a][b] != 'B':
                        idx1 += 1
                    if l[a][b] != 'W':
                        idx2 += 1
        count.append(min(idx1,idx2))

print(min(count))