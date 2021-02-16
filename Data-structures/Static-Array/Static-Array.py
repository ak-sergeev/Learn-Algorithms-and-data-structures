class Array:
    """
    Линейный статический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполненного массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        # Проверяем заполненность массива.
        if self.length == self.size:
            raise OverflowError

        # Добавляем новый элемент.
        self.data[self.length] = value

        # Увеличиваем длину.
        self.length += 1
        
    def insert(self, index, value):
        """
        Добавление нового элемента со значением value на позицию index.
        """
        if self.length == self.size:
            raise OverflowError

        # Проверка выхода индекса за пределы.
        if index > self.length:
            # Просто вставляем в конец.
            self.append(value)
            return

        # Сперва копируем элементы.
        end_index = self.length  # Начинаем с последнего элемента
        while end_index > index:
            self.data[end_index] = self.data[end_index - 1]
            end_index -= 1

        # Теперь вставляем новый элемент
        self.data[index] = value

        # Увеличиваем длину
        self.length += 1
        
    def reverse(self):
        """
        Разворачивает массив.
        """

        left = 0
        # Перебираем половину массива
        while left < self.length // 2:
            right = (self.length - 1) - left

            # Обмен значениями
            buf = self.data[left]
            self.data[left] = self.data[right]
            self.data[right] = buf

            # Альтернативный вариант обмена в стиле Python
            # self.data[left], self.data[right] = self.data[right], self.data[left]

            left += 1
            
    def remove(self, value):
        """
        Удаляет элементы со значением value.
        Время работы O(N).

        Суть алгоритма: проходим в цикле по всем элементам.
        Если встречаем элемент для удаления, то увеличиваем shift на единицу и переходим к следующему.
        Если встречаем обычный элемент, то сдвигаем его влево на shift позиций.
        """

        i = shift = 0
        while i < self.length:
            if self.data[i] == value:
                # Увеличиваем сдвиг
                shift += 1
            else:
                # Сдвигаем элемент влево на shift позиций.
                self.data[i - shift] = self.data[i]

            i += 1

        self.length -= shift
        
    def min(self):
        """
        Минимальное значение в массиве.
        """
        _min = self.data[0] if self.data else None
        i = 1
        while i < self.length:
            if self.data[i] < _min:
                _min = self.data[i]
            i += 1
        return _min

    def max(self):
        """
        Максимальное значение в массиве.
        """
        _max = self.data[0] if self.data else None
        i = 1
        while i < self.length:
            if self.data[i] > _max:
                _max = self.data[i]
            i += 1
        return _max

    def avg(self):
        """
        Среднее значение в массиве.
        """
        _sum = 0
        i = 0
        while i < self.length:
            _sum += self.data[i]
            i += 1
        return _sum / self.length    
    
    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"




def merge(array1, array2):
    """
    Функция слияния двух отсортированных массивов в один.
    """

    # Итоговый массив.
    array = []

    # Определяем начальные индексы.
    i = j = 0

    # Проходим в цикле, пока один из массивов не закончится.
    while i < len(array1) and j < len(array2):

        # Помещаем меньший элемент в новый массив и увеличиваем счетчик.
        if array1[i] <= array2[j]:
            array.append(array1[i])
            i += 1
        else:
            array.append(array2[j])
            j += 1

    # Проходим в цикле по оставшимся частям массивов.
    while i < len(array1):
        array.append(array1[i])
        i += 1

    while j < len(array2):
        array.append(array2[j])
        j += 1

    return array
