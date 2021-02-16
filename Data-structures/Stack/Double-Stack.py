class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    """
    Двойной стек на базе статического массива.
    """

    def __init__(self, size):
        super().__init__(size)

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
        self.length = 0
