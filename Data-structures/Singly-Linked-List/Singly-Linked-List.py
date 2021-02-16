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

        return
    
    def sort(self):
        """
        Сортирует связный список методом выбора.
        Хорошо работает при частых добавлениях новых элементов и при редких сортировках.
        """

        # Новый ограничитель для нового списка.
        new_top = Node()

        current = self.top

        # Повторяем пока исходный список не пустой.
        while current.next_node is not None:

            # Ячейка after_me предшествует ячейке с наибольшим элементом.
            max_after_me = current
            max_value = max_after_me.next_node.value

            # Ищем следующий элемент
            after_me = current.next_node
            while after_me.next_node is not None:
                if after_me.next_node.value > max_value:
                    max_after_me = after_me
                    max_value = after_me.next_node.value
                after_me = after_me.next_node

            # Удаляем максимальную ячейку из текущего списка.
            max_node = max_after_me.next_node
            max_after_me.next_node = max_node.next_node

            # Добавлям максимальную ячейку в начало нового списка.
            max_node.next_node = new_top.next_node
            new_top.next_node = max_node

        self.top = new_top

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
