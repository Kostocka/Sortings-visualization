# from sorts import bubble_sort, merge_sort

# def test_sort(sort_func, name=""):
#     assert sort_func([]) == []
#     assert sort_func([1]) == [1]
#     assert sort_func([2, 1]) == [1, 2]
#     assert sort_func([3, 2, 1]) == [1, 2, 3]
#     assert sort_func([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]
#     assert sort_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
#     assert sort_func([5, 5, 5, 5]) == [5, 5, 5, 5]
#     assert sort_func([10, -1, 2, 5, 0]) == [-1, 0, 2, 5, 10]
#     print("Все тесты прошли!")

# if __name__ == "__main__":
#     test_sort(lambda arr: bubble_sort(arr), "Bubble Sort")
#     test_sort(lambda arr: merge_sort(arr)[0], "Merge Sort")

from sorts import bubble_sort, merge_sort
from visualize import visualize_sort

if __name__ == "__main__":
    arr = [5, 3, 8, 1, 2 , 4 , 1]
    visualize_sort(arr, bubble_sort)

    visualize_sort(arr, merge_sort)
