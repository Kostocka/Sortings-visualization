from visualize import visualize_sort
from sorts import bubble_sort , merge_sort , quick_sort
import random

if __name__ == "__main__":
    n = int(input("Введите размер массива ") )
    arr = [random.randint(1, 100) for _ in range(n)]

    sortings = {
        "bubble": bubble_sort,
        "merge": merge_sort,
        "quick" : quick_sort
    }

    sort_name = input("Введите какую сортировку изобразить (bubble, merge , quick): ").strip().lower()

    if sort_name in sortings:
        visualize_sort(arr, sortings[sort_name])
    else:
        print("Неизвестная сортировка. Доступные варианты: bubble, merge , quick_sort.")
