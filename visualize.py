# import time
# import os

# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def print_array(arr, highlights=None):
#     color_reset = "\033[0m"
#     color_codes = {
#         "yellow": "\033[93m",
#         "red": "\033[91m",
#         "green": "\033[92m",
#         "blue": "\033[94m",
#         "magenta": "\033[95m",
#     }

#     output = []
#     for i, val in enumerate(arr):
#         color = color_reset
#         if highlights and i in highlights:
#             color = color_codes.get(highlights[i], color_reset)
#         output.append(f"{color}{val}{color_reset}")
#     print(" ".join(output))

# def visualize_sort(arr, sort_func):
#     arr_copy = arr.copy()
#     sorted_arr, steps = sort_func(arr_copy)

#     for step in steps:
#         clear_console()

#         highlights = {}

#         if step[0] == 'compare':
#             i, j = step[1], step[2]
#             highlights[i] = "yellow"
#             highlights[j] = "yellow"

#         elif step[0] == 'swap':
#             i, j = step[1], step[2]
#             highlights[i] = "red"
#             highlights[j] = "red"
#             arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]

#         elif step[0] == 'split':
#             l, r = step[1], step[2]
#             for idx in range(l, r+1):
#                 highlights[idx] = "blue"

#         elif step[0] == 'merge':
#             l, r = step[1], step[2]
#             for idx in range(l, r+1):
#                 highlights[idx] = "magenta"

#         elif step[0] == 'overwrite':
#             idx, value = step[1], step[2]
#             arr_copy[idx] = value
#             highlights[idx] = "green"

#         print_array(arr_copy, highlights)
#         time.sleep(0.5)  # Задержка между кадрами

#     clear_console()
#     print_array(arr_copy)

import matplotlib.pyplot as plt

def print_array(arr, highlights=None):
    plt.clf()
    colors = ['lightgray'] * len(arr)

    if highlights:
        for idx, color in highlights.items():
            colors[idx] = color

    plt.bar(range(len(arr)), arr, color=colors)
    plt.pause(0.3)

def visualize_sort(arr, sort_func):
    arr_copy = arr.copy()
    sorted_arr, steps = sort_func(arr_copy)

    plt.ion()
    fig = plt.figure()

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
            l, r = step[1], step[2]
            for idx in range(l, r+1):
                highlights[idx] = "blue"

        elif step[0] == 'merge':
            l, r = step[1], step[2]
            for idx in range(l, r+1):
                highlights[idx] = "magenta"

        elif step[0] == 'overwrite':
            idx, value = step[1], step[2]
            arr_copy[idx] = value
            highlights[idx] = "green"

        print_array(arr_copy, highlights)

    plt.ioff()
    plt.show()
