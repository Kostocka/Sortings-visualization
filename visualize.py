import matplotlib.pyplot as plt

def print_array(arr, highlights=None, active_range=None):
    plt.clf()
    n = len(arr)
    colors = ['lightgray'] * n

    if active_range:
        l, r = active_range
        for i in range(l, r+1):
            colors[i] = 'skyblue' 

    if highlights:
        for idx, color in highlights.items():
            colors[idx] = color

    plt.bar(range(n), arr, color=colors, width=0.8)
    plt.xlim(-1, n)
    plt.ylim(0, max(arr) * 1.1)
    plt.pause(0.1)

def visualize_sort(arr, sort_func):
    arr_copy = arr.copy()
    sorted_arr, steps = sort_func(arr_copy)

    plt.ion()
    fig = plt.figure()

    active_range = None
    pivot_idx = None 

    for step in steps:
        highlights = {}

        if step[0] == 'compare':
            i, j = step[1], step[2]
            highlights[i] = "yellow"
            highlights[j] = "yellow"

        elif step[0] == 'swap':
            i, j = step[1], step[2]
            highlights[i] = "red"
            highlights[j] = "red"
            arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]

        elif step[0] == 'split':
            l, r, _ = step[1], step[2], step[3]
            active_range = (l, r)

        elif step[0] == 'pivot':
            pivot_idx = step[1]

        elif step[0] == 'merge':
            l, r, _ = step[1], step[2], step[3]
            active_range = (l, r)

        elif step[0] == 'overwrite':
            if len(step) == 5:
                idx, value, l, r = step[1], step[2], step[3], step[4]
                active_range = (l, r)
            else:
                idx, value = step[1], step[2]
            arr_copy[idx] = value
            highlights[idx] = "limegreen"

        if pivot_idx is not None:
            highlights[pivot_idx] = "purple" 

        print_array(arr_copy, highlights, active_range)

    highlights = {i: "limegreen" for i in range(len(arr_copy))}
    print_array(arr_copy, highlights)

    plt.ioff()
    plt.show()
