#Sort Algorithm
#O(n^2) 인 알고리즘 사용하기
#Selection Sort
#Insertion Sort
#Bubble Sort

import sys
#Selection Sort
#최솟값을 찾아 최솟값 부터 앞에 쌓기
def SelectionSort(arr):
    for i in range(len(arr)-1):
        minidx = i
        for j in range(i, len(arr)):
            if arr[minidx] > arr[j]:
                minidx = j
        
        arr[minidx], arr[i] = arr[i], arr[minidx]

#InsertionSort
#두번째 자료로 시작하여 그 앞의 자료와 비교하여 insert할 위치를 지정하는 알고리즘

def InsertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i, 0,-1):
            if arr[i] < arr[j-1]:
                arr[i],arr[j-1] = arr[j-1],arr[i]

#BubbleSort
#서로 인접한 두 원소를 검사
#1회전 후 가장 큰 값이 가장 오른쪽으로 이동
#이 과정을 반복하는 알고리즘
def BubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(input()))

# SelectionSort(l)
# InsertionSort(l)
BubbleSort(l)
for i in l:
    print(i)