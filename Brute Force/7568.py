import sys

n = int(sys.stdin.readline())
#덩치크기 순위 정하기 문제
l = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split())) #(55, 185)를 list화해서 입력
    l.append(a)


ans = []
for i in range(n):
    c = 1
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            c += 1
    ans.append(c)

print(*ans) #list를 []없이 출력
    
