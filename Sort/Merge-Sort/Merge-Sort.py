def mergesort(array):
    """
    Подготовка к сортировке слиянием.
    Сложность O(N*logN)
    Устойчив
    """
    
    # Создаем временный массив
    temp_array = [None] * len(array)

    # Сортировка
    do_mergesort(array, temp_array, 0, len(array) - 1)


def do_mergesort(array, temp_array, start, end):
    """
    Сортировка массива сортировкой слиянием.
    """
    
    # Если массив содержит только один элемент, значит он отсортирован.
    if start == end:
        return

    # Ищем средний элемент, который разбивает массив на две части.
    midpoint = (start + end) // 2
    
    # Вызываем сортировку слиянием для левой и правой частей массива.
    do_mergesort(array, temp_array, start, midpoint)
    do_mergesort(array, temp_array, midpoint + 1, end)

    # Слияние двух отсортированных массивов.
    # На этом этапе левая и правая часть массива отсортирована.
    left_index = start
    right_index = midpoint + 1
    temp_array_index = left_index
    while (left_index <= midpoint) and (right_index <= end):
        if array[left_index] <= array[right_index]:
            temp_array[temp_array_index] = array[left_index]
            left_index += 1
        else:
            temp_array[temp_array_index] = array[right_index]
            right_index += 1
        temp_array_index += 1

    # Финальное копирование непустых массивов.
    for i in range(left_index, midpoint + 1):
        temp_array[temp_array_index] = array[i]
        temp_array_index += 1
    for i in range(right_index, end + 1):
        temp_array[temp_array_index] = array[i]
        temp_array_index += 1

    # Обратное копирование временного массива в основной.
    for i in range(start, end + 1):
        array[i] = temp_array[i]
