def countingsort(values, max_value):
    """
    Сортировка подсчетом.
    Работает с массивами целых чисел в небольшом диапазоне.
    
    """

    # Создаем массив-счетчик.
    counts = [0] * (max_value + 1)

    # Считаем количество значений основного массива.
    for value in values:
        counts[value] += 1

    # Копируем значения обратно в массив.
    index = 0
    for i in range(max_value + 1):
        for j in range(counts[i]):
            values[index] = i
            index += 1


# data = [1, 2, 2, 1, 0, 2, 2, 1, 0, 2]
# countingsort(data, 2)
# print(data)
