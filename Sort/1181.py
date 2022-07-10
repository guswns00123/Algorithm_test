import sys

n = int(sys.stdin.readline())
word_list = []
for i in range(n):
    word_list.append(input())

word_list = list(set(word_list))
word_list.sort(key = lambda x: (len(x),x))
#len(x)의 길이로 정렬후 같다면 x, 즉, 단어 알파벳순으로 정렬한다는 뜻


for i in word_list:
    print(i)