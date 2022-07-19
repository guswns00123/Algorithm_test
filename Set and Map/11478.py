import sys

str = sys.stdin.readline().rstrip()

str2 = []
for i in range(len(str)):
    for j in range(i, len(str)+1):
        str2.append(str[i:j])
#문자열에서 모든 경우의수를 찾기

res = set(str2)
#집합을 이용하여 중복을 제거
print(len(res)-1)
