import random


class Vector:
    """
    Klasa Vector przechowująca kolekcję liczb.
    """

    def __init__(self, size=3):
        """
        Konstruktor przyjmujący rozmiar wektora jako argument (domyślnie 3).
        """
        self._values = [0] * size

    def randomize(self):
        """
        Metoda do losowej generacji elementów wektora.
        """
        for i in range(len(self._values)):
            self._values[i] = random.random()

    def read_values(self, values):
        """
        Metoda do wczytywania elementów wektora z listy podanej jako argument.
        """
        if len(values) != len(self._values):
            raise ValueError("Vector size mismatch.")
        self._values = values

    def __add__(self, other):
        """
        Operator dodawania dwóch wektorów.
        """
        if len(self._values) != len(other._values):
            raise ValueError("Vector size mismatch.")
        result = Vector(len(self._values))
        for i in range(len(self._values)):
            result[i] = self._values[i] + other._values[i]
        return result

    def __sub__(self, other):
        """
        Operator odejmowania dwóch wektorów.
        """
        if len(self._values) != len(other._values):
            raise ValueError("Vector size mismatch.")
        result = Vector(len(self._values))
        for i in range(len(self._values)):
            result[i] = self._values[i] - other._values[i]
        return result

    def __mul__(self, scalar):
        """
        Mnożenie wektora przez skalar.
        """
        result = Vector(len(self._values))
        for i in range(len(self._values)):
            result[i] = self._values[i] * scalar
        return result

    def length(self):
        """
        Metoda wyliczająca długość wektora.
        """
        return sum(x ** 2 for x in self._values) ** 0.5

    def sum(self):
        """
        Metoda wyliczająca sumę elementów wektora.
        """
        return sum(self._values)

    def dot_product(self, other):
        """
        Metoda wyliczająca iloczyn skalarny dwóch wektorów.
        """
        if len(self._values) != len(other._values):
            raise ValueError("Vector size mismatch.")
        return sum(self._values[i] * other._values[i] for i in range(len(self._values)))

    def __repr__(self):
        """
        Reprezentacja tekstowa wektora.
        """
        return f"Vector({self._values})"

    def __getitem__(self, index):
        """
        Operator [] pozwalający na dostęp do konkretnych elementów wektora.
        """
        return self._values[index]

    def __contains__(self, item):
        """
        Operator in sprawdzający przynależność elementu do wektora.
        """
        return item in self._values


if __name__ == "__main__":
    v1 = Vector()
    print(v1)
    v1.randomize()
    print(v1)
    v2 = Vector()

if __name__ == "__main__":
    # test konstruktora
    v1 = Vector()
    assert str(v1) == "Vector([0, 0, 0])"
    v2 = Vector(5)
    assert str(v2) == "Vector([0, 0, 0, 0, 0])"

    # test losowej generacji elementów wektora
    v1.randomize()
    assert all(isinstance(x, float) and 0 <= x <= 1 for x in v1)

    # test wczytywania elementów wektora z listy
    v2.read_values([1, 2, 3, 4, 5])
    assert str(v2) == "Vector([1, 2, 3, 4, 5])"

    # test operatora dodawania dwóch wektorów
    v3 = v1 + v2
    assert str(
        v3) == "Vector([2.701661535301984, 2.068933693298199, 3.618425033500089, 4.034708411135715, 5.819219682291862])"

    # test operatora odejmowania dwóch wektorów
    v4 = v1 - v2
    assert str(
        v4) == "Vector([-0.7016615353019837, -1.068933693298199, -2.618425033500089, -3.0347084111357146, -4.819219682291862])"

    # test mnożenia wektora przez skalar
    v5 = v1 * 2
    assert str(v5) == "Vector([1.4164860141964104, 0.9461317502414848, 1.8589215430086674])"

    # test wyliczania długości wektora
    assert abs(v1.length() - 1.0) < 1e-6
    assert abs(v2.length() - 7.416198487095663) < 1e-6

    # test wyliczania sumy elementów wektora
    assert v1.sum() > 0

    # test wyliczania iloczynu skalarnego dwóch wektorów
    assert abs(v1.dot_product(v2) - 13.040799669974498) < 1e-6

    # test operatora []
    assert v1[0] == v1._values[0]

    # test operatora in
    assert 0.5 in v1
    assert 2.5 not in v1

    print("All tests passed.")
