import sys

n, m = map(int,sys.stdin.readline().split())

poket_dex = []
quiz = []

for i in range(n+m):
    if i < n: poket_dex.append(sys.stdin.readline().rstrip())
    else: 
        quiz.append(sys.stdin.readline().rstrip())

poket_dex_dic = {poket_dex[i] : str(i+1) for i in range(len(poket_dex))}
# print(poket_dex_dic)
# print(quiz)
list_key = list(poket_dex_dic.keys())

for i in quiz:
    if i in poket_dex_dic.keys():
        print(poket_dex_dic[i])
    else:
        print(list_key[int(i)-1])

