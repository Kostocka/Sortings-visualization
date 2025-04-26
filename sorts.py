# def swap(arr, i, j):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp

def bubble_sort(arr):
    n = len(arr)
    arr = arr.copy()
    steps = []
    
    for i in range(n):
        for j in range(n-i-1):
            steps.append(('compare', j, j+1))
            if arr[j] > arr[j+1]:
                steps.append(('swap', j, j+1))
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, steps

def merge_sort(arr):
    arr = arr.copy()
    steps = []

    def splitting(l, r, depth):
        if l >= r:
            return
        m = (l + r) // 2
        steps.append(('split', l, m, depth))
        steps.append(('split', m+1, r, depth))
        splitting(l, m, depth + 1)
        splitting(m+1, r, depth + 1)
        merge(l, m, r, depth)

    def merge(l, m, r, depth):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            steps.append(('compare', l+i, m+1+j))
            if left[i] <= right[j]:
                arr[k] = left[i]
                steps.append(('overwrite', k, arr[k], l, r))
                i += 1
            else:
                arr[k] = right[j]
                steps.append(('overwrite', k, arr[k], l, r))
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            steps.append(('overwrite', k, arr[k], l, r))
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            steps.append(('overwrite', k, arr[k], l, r))
            j += 1
            k += 1

        steps.append(('merge', l, r, depth))

    splitting(0, len(arr) - 1, 0)
    return arr, steps
