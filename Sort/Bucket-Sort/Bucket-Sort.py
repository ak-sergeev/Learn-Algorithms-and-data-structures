class Cell:
    """
    Ячейка для сортированного связного списка.
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


def bucketsort(array, num_buckets):
    """
    Блочная сортировка массива array.
    Эффективная блочная сортировка должна удовлетворять трём условиям:
    1. Равномерное распределение значений в массиве.
    2. Корзины (блоки) должны идти в возрастающем порядке.
    3. Количество корзин должно быть соизмеримо с количеством элементов в массиве. Это требует N дополнительной памяти, но тогда сортировка стремится к времени O(N)
    """

    # Создаем блоки, в которые помещаем пустые связные списки.
    buckets = []
    for i in range(num_buckets):
        buckets.append(Cell())

    # Вычисляем максимальный элемент в массиве.
    # Можно просто написать max_value = max(array)
    i = 0
    max_value = array[i]
    while i < len(array):
        if array[i] > max_value:
            max_value = array[i]
        i += 1

    # Рассчитываем количество значений в корзине.
    items_per_bucket = (max_value + 1) / num_buckets

    # Распределяем данные по корзинам.
    for value in array:
        # Вычисляем номер корзины.
        backet_num = int(value / items_per_bucket)

        # Вставляем элемент в корзину сразу со сортировкой.
        after_me = buckets[backet_num]
        while (after_me.next_node is not None) and (after_me.next_node.value < value):
            after_me = after_me.next_node
        cell = Cell(value, after_me.next_node)
        after_me.next_node = cell

    # Отправляем элементы обратно в массив.
    index = 0
    for i in range(num_buckets):
        # Копируем значения из корзины в массив.
        cell = buckets[i].next_node
        while cell is not None:
            array[index] = cell.value
            index += 1
            cell = cell.next_node
