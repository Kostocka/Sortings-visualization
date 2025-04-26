from sorts import bubble_sort

def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert bubble_sort([10, -1, 2, 5, 0]) == [-1, 0, 2, 5, 10]
    print("Все тесты прошли!")

if __name__ == "__main__":
    test_bubble_sort()