#Sort Algorithm
#O(nlogn) 인 알고리즘 사용하기
#Quick Sort
#Heap Sort
#Merge Sort

import sys

def partition(arr,left, right):
    low = left
    high = right
    pivot = arr[left]

    while low < high:
        while low <= right and arr[low] < pivot:
            low += 1
        while high >= left and arr[high] > pivot:
            high -= 1
        if low < high : #만약 low와 high가 교차하지 않았으면 list[low] 와 list[high] 교환
            arr[low], arr[high] = arr[high], arr[low]

    #low와 high가 교차했으면 list[left]와 list[high]를 교환
    arr[left], arr[high] = arr[high], arr[left]

    return high #피벗의 위치인 high를 반환

def QuickSort(arr, left, right):
    print(arr)
    if left< right:
        pivot = partition(arr, left, right)
        print(pivot)
        QuickSort(arr, left, pivot-1)
        QuickSort(arr, pivot+1, right)

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(input()))

QuickSort(l,0, n-1)

for i in l:
    print(i)