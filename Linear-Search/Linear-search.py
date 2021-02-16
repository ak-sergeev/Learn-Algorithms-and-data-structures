def linear_search(values, target):
    """
    Линейный поиск.
    """
    i = 0

    # Перебираем массив в цикле
    while i < values.__len__():
        # Сравниваем искомое значение с очередным элементом массива.
        # Возвращаем значение, если элемент найден.
        if values[i] == target:
            return i

        # Ранний выход если массив отсортирован и искомый элемент больше текущего.
        if values[i] > target:
            return -1
        i += 1

    # Возвращаем -1 если элемент не найден.
    return -1