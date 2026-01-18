'''

Реализуйте класс Graph, представляющий неориентированный граф с вершинами, пронумерованными от 0 до V - 1:

    Конструктор Graph(V):

        Создаёт граф с V вершинами.

        Если V — отрицательное число, нужно сгенерировать исключение IllegalArgumentError.

    Метод add_edge(v, w):

        Добавляет ребро между вершинами v и w.

        Допускаются параллельные рёбра и самопетли.

            Самопетля v-v должна появиться дважды в списке смежности вершины v.

        Если v или w вне диапазона 0 ≤ v, w < V, выбросить исключение IllegalArgumentError.

    Метод adjacent(v):

        Возвращает список всех вершин, смежных с v.

        Если v недопустим, выбросить IllegalArgumentError.

    Методы V() и E():

        V() — возвращает количество вершин.

        E() — возвращает количество рёбер.

Дополнительные требования:

    Определите собственное исключение IllegalArgumentError (например, как подкласс Exception).

Sample Input:

Sample Output:

OK

'''

class IllegalArgumentError(Exception):
    """Исключение, выбрасываемое при передаче некорректных аргументов."""
    pass


class Graph:
    def __init__(self, V):
        if V < 0:
            raise IllegalArgumentError("Количество вершин не может быть отрицательным")
        self._V = V
        self._E_count = 0
        # Инициализируем список смежности: для каждой вершины — пустой список
        self._adj = [[] for _ in range(V)]

    def add_edge(self, v, w):
        if not (0 <= v < self._V) or not (0 <= w < self._V):
            raise IllegalArgumentError("Вершина вне допустимого диапазона")
        self._adj[v].append(w)
        self._adj[w].append(v)
        self._E_count += 1

    def adjacent(self, v):
        if not (0 <= v < self._V):
            raise IllegalArgumentError("Вершина вне допустимого диапазона")
        return self._adj[v]

    def V(self):
        return self._V

    def E(self):
        return self._E_count

    # Для совместимости с тестом: тест использует z.V, z.E, z.adj
    @property
    def V(self):
        return self._V

    @property
    def E(self):
        return self._E_count

    @property
    def adj(self):
        return self._adj

# Не изменяйте написанный ниже код
def run_tests():
    success = True

    try:
        z = Graph(3)
        z.add_edge(2, 2)
        z.add_edge(0, 1)

        assert z.V == 3
        assert z.E == 2
        assert z.adj == [[1], [0], [2, 2]]
    except Exception as e:
        print(f"Test failed on Graph(3): {e}")
        success = False

    try:
        G = Graph(0)
        assert G.V == 0
        assert G.E == 0
        assert G.adj == []
    except Exception as e:
        print(f"Test failed on Graph(0): {e}")
        success = False

    try:
        Graph(-1)
        assert False, "Expected IllegalArgumentError but got nothing"
    except IllegalArgumentError:
        pass
    except Exception as e:
        print(f"Test failed on Graph(-1): {e}")
        success = False

    try:
        G = Graph(15)
        msg = "Expect to throw an IllegalArgumentError unless 0 <= vertex < V"

        G.add_edge(-1, 4)
        assert False, msg + " (-1, 4)"
    except IllegalArgumentError:
        pass
    except Exception as e:
        print(f"Test failed on add_edge(-1, 4): {e}")
        success = False

    try:
        G.add_edge(1, -4)
        assert False, msg + " (1, -4)"
    except IllegalArgumentError:
        pass
    except Exception as e:
        print(f"Test failed on add_edge(1, -4): {e}")
        success = False

    try:
        G.add_edge(5, 15)
        assert False, msg + " (5, 15)"
    except IllegalArgumentError:
        pass
    except Exception as e:
        print(f"Test failed on add_edge(5, 15): {e}")
        success = False

    if success:
        print("OK")
    else:
        print("Failed")

run_tests()