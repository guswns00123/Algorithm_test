import sys


n = int(sys.stdin.readline())
a = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append([x,y])

a.sort(key = lambda x:(x[1], x[0]))
#두번째 값이 같을 경우 첫번째 값을 기준으로 오름차순 정렬한다는 뜻

#sort에 key값으로 y값 기준으로 정렬하게 변경
#sort.(key = lambda x:x[0]) ==> 행기준으로 정렬 + x:x[0] 에서 x:-x[0]으로 변경시 내림차순정렬 가능
#sort.(key = lambda x:x[1]) ==> 열기준으로 정렬

for i in range(n):
    print(*a[i])