class Stack:
    """
    Двойной стек.
    """

    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

        # Задаем указатели за пределами
        self.top_left = -1
        self.top_right = self.size

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        if self.top_left >= 0:
            value = self.data[self.top_left]
            self.top_left -= 1
            self.length -= 1
            return value

    def is_left_empty(self):
        """
        Пустая ли левая часть стека?
        """
        return self.top_left == -1

    def is_right_empty(self):
        """
        Пустая ли правая часть стека?
        """
        return self.top_right == self.size

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        # Добавьте ваш код тут

        if self.top_right < self.size:
            value = self.data[self.top_right]
            self.top_right += 1
            self.length -= 1
            return value

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева
        """
        # Проверяем заполненность стека.
        if self.length == self.size:
            raise OverflowError

        # Смещаем указатель.
        self.top_left += 1

        # Увеличиваем длину
        self.length += 1

        # Добавляем новый элемент.
        self.data[self.top_left] = value

    def push_right(self, value):
        # Проверяем заполненность стека.
        if self.length == self.size:
            raise OverflowError

        # Смещаем указатель.
        self.top_right -= 1

        # Увеличиваем длину
        self.length += 1

        # Добавляем новый элемент.
        self.data[self.top_right] = value

    def clear(self):
        self.top_left = -1
        self.top_right = self.size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data)) + "]"


def quicksort(array):
    """
    Основная функция быстрой сортировки.
    Принимает только массив array.
    """
    # Создаем стек размером с массив -1 элемент (разделитель в стек не попадает).
    stack = Stack(len(array) - 1)
    # Запуск основной функции сортировки.
    do_quicksort(array, stack, 0, len(array) - 1)


def do_quicksort(array, stack, start, end):
    """
    Быстрая сортировка c использованием двойного стека.
    Передаем исходный массив, двойной стек и индексы подмассива для сортировки.
    """
    if start >= end:
        return

    divider = array[start]

    # Помещаем элементы до и после от разделителя.
    i = start + 1
    while i < end + 1:
        if array[i] < divider:
            # Помещаем элемент в левую часть стека.
            stack.push_left(array[i])
        else:
            # Помещаем элемент в правую часть стека.
            stack.push_right(array[i])
        i += 1

    # Помещаем элементы до разделителя обратно в массив.
    index = start
    # Выполняем цикл, до тех пор, пока левая часть стека не окажется пустой.
    while not stack.is_left_empty():
        # Извлекаем элемент из левой части стека обратно в массив.
        array[index] = stack.pop_left()
        index += 1

    # Вставляем разделитель.
    array[index] = divider

    # Запоминаем, что это средняя точка.
    midpoint = index

    # Добавляем элементы после разделителя,
    index += 1
    # Выполняем цикл, до тех пор, пока правая часть стека не окажется пустой.
    while not stack.is_right_empty():
        # Извлекаем элемент из правой части стека обратно в массив.
        array[index] = stack.pop_right()
        index += 1

    # Сортируем две половинки массива.
    do_quicksort(array, stack, start, midpoint - 1)
    do_quicksort(array, stack, midpoint + 1, end)
