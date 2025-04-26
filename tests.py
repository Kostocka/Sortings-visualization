from visualize import visualize_sort
from sorts import bubble_sort , merge_sort , quick_sort

if __name__ == "__main__":
    arr = [5, 3, 8, 1, 2 , 4 , 1]
    # arr = [ 9 ,8 ,7 ,6,5,4,3,2,1]

    sortings = {
        "bubble": bubble_sort,
        "merge": merge_sort,
        "quick" : quick_sort
    }

    sort_name = input("Введите какую сортировку изобразить (bubble или merge): ").strip().lower()

    if sort_name in sortings:
        visualize_sort(arr, sortings[sort_name])
    else:
        print("Неизвестная сортировка. Доступные варианты: bubble, merge , quick_sort.")
