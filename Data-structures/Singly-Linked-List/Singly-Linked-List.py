class Node:
    """
    Класс ячейки
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

# Создаем интерфейс работы со связным списком на базе класса List
class List:
    """
    Класс для работы со списком
    """
    def __init__(self):
        self.top = Node(None)
        self.tail = None

    def append(self, value):
        """
        Добавление нового элемента в конец связного списка.
        """
        new_node = Node(value)

        # Если нет head (или другими словами top.next_node), значит и нет tail
        if self.top.next_node is None:
            self.top.next_node = new_node
            self.tail = new_node
            return

        # Обмен значениями - быстрая вставка за время O(1)
        self.tail.next_node = new_node
        self.tail = new_node
        
    def prepend(self, value):
        """
        Добавляем элемент в начало
        """
        new_node = Node(value)
        new_node.next_node = self.top.next_node
        self.top.next_node = new_node
        
    def delete(self, value):
        """
        Удаление элемента по значению.
        Время работы O(N).
        """

        # Задаем текущий и предыдущие элементы.
        current = self.top.next_node
        prev = self.top

        # Перебираем элементы и ищем тот, который надо удалить
        while current is not None:
            if current.value == value:
                # Если нашли, то просто меняем ссылку.
                prev.next_node = current.next_node
                return

            # Обновляем текущий и предыдущий элементы.
            prev = current
            current = current.next_node

    def insert(self, value, after_value):
        """
        Вставка нового элемента в середину связного списка.
        После значения after_value
        """

        has_after_value = False

        # Перебираем по очереди все элементы, чтобы найти нужный
        current = self.top
        while current is not None:
            if current.value == after_value:
                has_after_value = True
                break
            current = current.next_node

        # Вставляем новый элемент после current
        if has_after_value:
            new_node = Node(value)
            new_node.next_node = current.next_node
            current.next_node = new_node
            
    def find(self, key):
        """
        Поиск значения по его ключу.
        """
        current = self.top.next_node

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next_node

        return None
        
    def length(self):
        i = 0
        current = self.top.next_node
        while current is not None:
            current = current.next_node
            i += 1

        return i

    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
