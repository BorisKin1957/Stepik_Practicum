def is_symmetric(root: tuple(int,tuple, tuple)) -> bool:
    """
    Проверяет, является ли двоичное дерево симметричным (зеркальным относительно корня).
    Аргументы:
        root: кортеж вида (значение, левое_поддерево, правое_поддерево) или None.
    """
    # Если дерево пустое (корень None), считаем его симметричным
    if root is None:
        return True

    # Распаковываем корень на значение, левое и правое поддеревья
    _, left, right = root

    # Проверяем, являются ли левое и правое поддеревья зеркальными
    return is_mirror(left, right)


def is_mirror(left, right):
    """
    Рекурсивно проверяет, являются ли два поддерева зеркальным отражением друг друга.
    Аргументы:
        left: левое поддерево (кортеж или None)
        right: правое поддерево (кортеж или None)

    """
    # Базовый случай: если оба поддерева пусты — они симметричны
    if left is None and right is None:
        return True

    # Если одно из деревьев пустое, а другое — нет, симметрии нет
    if left is None or right is None:
        return False

    # Распаковываем оба узла: значение, левое и правое поддеревья
    l_val, l_left, l_right = left
    r_val, r_left, r_right = right

    # Проверяем:
    # 1. Значения в узлах совпадают
    # 2. Левое поддерево left зеркально правому поддереву right
    # 3. Правое поддерево left зеркально левому поддереву right
    return (l_val == r_val and
            is_mirror(l_left, r_right) and
            is_mirror(l_right, r_left))


# tree1: (1, (2, (3, None, None), (4, None, None)), (2, (4, None, None), (3, None, None)))
tree1 = (1,
         (2,
          (3, None, None),
          (4, None, None)),
         (2,
          (4, None, None),
          (3, None, None)))

# tree2: (1, (2, (3, None, None), (5, None, None)), (2, (6, None, None), (3, None, None)))
tree2 = (1,
         (2,
          (3, None, None),
          (5, None, None)),
         (2,
          (6, None, None),
          (3, None, None)))

# tree3: (1, (2, (5, None, None), None), (2, None, (5, None, None)))
tree3 = (1,
         (2,
          (5, None, None),
          None),
         (2,
          None,
          (5, None, None)))

print(is_symmetric(tree1))  # True
print(is_symmetric(tree2))  # False
print(is_symmetric(tree3))  # True