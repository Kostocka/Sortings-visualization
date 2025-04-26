def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)
    return arr