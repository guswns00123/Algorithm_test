import sys
#좌표 정렬하기
#2차 배열 함수 정렬도 sort함수 똑같이 적용가능

n = int(sys.stdin.readline())
a = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append([x,y])




a.sort()
for i in range(n):
    print(*a[i])