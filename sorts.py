def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    n = len(arr)
    arr = arr.copy()
    steps = []
    
    for i in range(n):
        for j in range(n-i-1):
            steps.append(('compare', j, j+1))
            if arr[j] > arr[j+1]:
                steps.append(('swap', j, j+1))
                swap(arr,j,j+1)
    return arr , steps

def merge_sort(arr):
    arr = arr.copy()
    steps = []

    def splitting(l , r , depth):
        if l >= r:
            return
        m = ( l + r ) // 2
        steps.append(('split', l, m))
        steps.append(('split', m+1, r))
        splitting(l , m , depth + 1)
        splitting(m+1 , r , depth + 1)
        merge(l,m,r)

    def merge(l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i = j = 0
        for k in range(l, r+1):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            steps.append(('overwrite', k, arr[k]))
        steps.append(('merge', l, r))

    splitting(0, len(arr)-1, 0)
    return arr, steps
