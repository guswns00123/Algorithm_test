import sys
# 숫자 정렬하기
# 숫자를 내림 차순으로 정렬한후 
# 내림차순으로 출력
arr = []
num = int(sys.stdin.readline())

while True:
    if num == 0:
        break
    a = num % 10
    arr.append(a)
    num = num // 10

arr.sort(reverse = True)
# print(arr)
sum = 0    
c = len(arr)-1
for i in range(len(arr)):
    sum += arr[i] * 10**c
    c -= 1

print(sum)