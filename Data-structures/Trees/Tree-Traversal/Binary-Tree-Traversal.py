class BinaryNode:
    """
    Класс узла для бинарного дерева
    """
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)

#  Все алгоритмы выполняются за время O(N)
def direct(node):
    """
    ОБХОД В ПРЯМОМ ПОРЯДКЕ.
    Сперва обрабатывается вершина, затем левый потомок, а после правый.
    """
    print(node.value, end="  ")
    if node.left_child:
        direct(node.left_child)
    if node.right_child:
        direct(node.right_child)


def symmetric(node):
    """
    СИММЕТРИЧНЫЙ ОБХОД.
    Сперва обрабатывается левый потомок, затем вершина, а после правый.
    Сортирует двоичное дерево поиска.
    """
    if node.left_child:
        symmetric(node.left_child)
    print(node.value, end="  ")
    if node.right_child:
        symmetric(node.right_child)

def reverse(node):
    """
    ОБХОД В ОБРАТНОМ ПОРЯДКЕ.
    Сперва обрабатывается левый потомок, затем правый, а после вершина.
    """
    if node.left_child:
        reverse(node.left_child)
    if node.right_child:
        reverse(node.right_child)
    print(node.value, end="  ")
