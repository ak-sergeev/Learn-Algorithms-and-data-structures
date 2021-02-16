def bubblesort(array):
    """
    Алгоритм пузырьковой сортировки массива в обратном порядке.
    """

    is_sorted = False
    while not is_sorted:

        is_sorted = True
        n = 1

        for i in range(len(array) - n):
            # Достаточно просто поменять знак сравнения.
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        n += 1
