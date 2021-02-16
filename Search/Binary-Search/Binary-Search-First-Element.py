import sys

val = int(sys.argv[1])
values = list(map(int, sys.argv[2:]))


def binary_search_rec(array, value, min_index=0, max_index=None):
    """
    Рекурсивный алгоритм.
    Возвращает индекс искомого элемента (value) в отсортированном массиве.
    Если в массиве более одного искомого элемента, то функция возвращает его первое вхождение.
    Если элемента в массиве нет, то возвращает -1.
    """
    if max_index is None:
        max_index = len(array) - 1

    if max_index >= min_index:
        # Вычисляем средний элемент.
        middle_index = min_index + (max_index - min_index) // 2

        # Условие выхода из рекурсии - первый элемент среди искомых.
        if (middle_index == 0 or value > array[middle_index - 1]) and array[middle_index] == value:
            return middle_index
        # Продолжаем поиск пока не найдем.
        elif value > array[middle_index]:
            return binary_search_rec(array, value, middle_index + 1, max_index)
        else:
            return binary_search_rec(array, value, min_index, middle_index - 1)
      
    return -1


def binary_search(array, value):
    """
    Возвращает индекс искомого элемента (value) в отсортированном массиве.
    Если в массиве более одного искомого элемента, то функция возвращает его первое вхождение.
    Если элемента в массиве нет, то возвращает -1.
    """

    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:
        middle_index = min_index + (max_index - min_index) // 2

        if (middle_index == 0 or value > array[middle_index - 1]) and array[middle_index] == value:
            return middle_index
        elif value > array[middle_index]:
            min_index = middle_index + 1
        else:
            max_index = middle_index - 1

    return -1


# Можно использовать любую из функций.
# print(binary_search(values, val))
# print(binary_search_rec(values, val))
