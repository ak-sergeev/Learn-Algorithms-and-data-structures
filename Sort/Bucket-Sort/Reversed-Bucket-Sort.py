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
    """

    # Создаем блоки, в которые помещаем пустые связные списки.
    buckets = []
    for i in range(num_buckets):
        buckets.append(Cell())

    # Вычисляем максимальны элемент в массиве.
    max_value = max(array)

    # Рассчитываем количество значений в корзине.
    items_per_bucket = (max_value + 1) / num_buckets

    # Распределяем данные по корзинам.
    for value in array:
        # Вычисляем номер корзины.
        backet_num = int(value / items_per_bucket)

        # Вставляем элемент в корзину сразу с обратной сортировкой.
        current = buckets[backet_num].next_node
        prev = buckets[backet_num]

        while current and current.value > value:
            prev = current
            current = current.next_node

        # Вставляем новую ячейку после предыдущей.
        new_cell = Cell(value)
        new_cell.next_node = prev.next_node
        prev.next_node = new_cell

    # Отправляем элементы обратно в массив.
    # При этом перебираем блоки в обратном порядке.
    b = num_buckets - 1
    index = 0
    while b >= 0:
        cell = buckets[b].next_node
        b -= 1

        while cell is not None:
            array[index] = cell.value
            index += 1
            cell = cell.next_node
