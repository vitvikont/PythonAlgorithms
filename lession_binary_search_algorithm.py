array = [23, 12, 14, 32, 19, 74, 93, 8, 103, 24, 54]


def binary_search(arr, search):
    # Алгоритм бинарного поиска в отсортированном массиве
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] < search:
            left = middle + 1  # Ищем в правой половине
        elif arr[middle] > search:
            right = middle - 1  # Ищем в левой половине
        else:
            return middle  # Элемент найден, вернуть индекс
    return -1  # Элемент не найден


if __name__ == '__main__':
    sorted(array)
    value = 93
    result = binary_search(array, value)
    print(result)
