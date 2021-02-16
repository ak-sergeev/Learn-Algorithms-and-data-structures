class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.next_node = next_node
        self.prev_node = prev_node
        self.value = value

    def __str__(self):
        return str(self.value)


class List:
    """
    Двунаправленный связный список.
    """
    def __init__(self):

        # Ограничитель
        self.top = Node()

    def append(self, value):
        """
        Добавление нового элемента в конец двунаправленного списка.
        Время работы O(N).
        """

        # Находим последнюю ячейку.
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Вставляем новую ячеку после current и делаем обратную ссылку.
        new_node = Node(value)
        current.next_node = new_node
        new_node.prev_node = current
      
    def prepend(self, value):
        """
        Добавление нового элемента в начало двунаправленного списка.
        """
        # Всего будет установлено 4 связи.
        new_node = Node(value)

        # Задаем связи для нового узла
        new_node.next_node = self.top.next_node
        new_node.prev_node = self.top

        # Ставим обратную связь для следующего узла (если он есть)
        # Связь на новый узел.
        if self.top.next_node:
            self.top.next_node.prev_node = new_node

        # Меняем ограничитель
        self.top.next_node = new_node

    def insert(self, after_value, value):
        """
        Добавление нового элемента value после элемента after_value.
        Время работы O(N).
        """

        # Находим ячейку перед той, в которую будем вставлять новый элемент.
        current = self.top.next_node
        while current is not None:
            if current.value == after_value:
                # Создаем новую ячейку
                new_node = Node(value, current.next_node, current)
                # Связываем впереди стоящий элемент с новой ячейкой
                if current.next_node is not None:
                    current.next_node.prev_node = new_node
                # Связываем предыдущий (текущий) элемент с новой ячейкой
                current.next_node = new_node
                return

            current = current.next_node
            
    def remove(self, value):
        """
        Удаление элемента из двунаправленного связного списка.
        """

        # Задаем начальные значения
        current = self.top.next_node
        prev = self.top

        while current is not None:
            if current.value == value:
                # Прямая связь для предыдущего элемента
                prev.next_node = current.next_node

                # Обратная связь для впереди стоящего элемента
                if current.next_node:
                    current.next_node.prev_node = prev

                return

            prev = current
            current = current.next_node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
