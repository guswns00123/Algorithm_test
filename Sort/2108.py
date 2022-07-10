import sys
import math
from collections import Counter

#산술평균
def mean(arr):
    res = round(sum(arr)/len(arr))
    return res

#중간값
def median(arr):
    res = arr[len(arr)//2]
    return res
#최빈값중 두번쨰로 작은 값
def mode(arr):
    # Counter => (키, 출현횟수)를 리턴
# most_common => 가장 많이 출현한 키를 n개 찾아줌 (리턴 값 : (키, 카운트))
    num = Counter(arr)
    modes = num.most_common()
    if len(arr) > 1 :
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod
# def mode(arr):

#     res = []
#     c = [0 for i in range(len(arr))]
#     for i in range(len(arr)):
#         if arr[i] in res:
#             for j in range(len(res)):
#                 if arr[i] == res[j]:
#                     idx = arr.index(arr[i])
#                     c[idx] += 1
#         else:
#             res.append(arr[i])
#             c[i] += 1
#     # print(*c)
#     tmp = max(c)
#     res2 = []
#     if max(c) in c:
#         for i in range(len(c)):
#             if tmp == c[i]:
#                 res2.append(arr[i])

#     # print(res2)
#     if len(res2) == 1:
#         return res2[0]
#     else:
#         return res2[1]
    



n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

print(mean(arr))
print(median(arr))
print(mode(arr))
print(max(arr) - min(arr))
