import sys
#ACM Hotel
#거리가 같을 때는 아래층 방 선호
#102호 보단 2101호 선호

n = int(sys.stdin.readline())

for i in range(n):
    h, w, m = map(int, sys.stdin.readline().split())
    # height = 6, width = 12 m = 10
    res = 1
    c = 0
    
    while(True):
            res += 100
            c += 1
            if (c == m) : break
            #print(res, c)
            if (c % h  == 0): res = res + 1 - h * 100 #맨꼭대기 층 가면 다시 1층오로
    print(res)
    

