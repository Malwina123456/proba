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
        #cos jest zle
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
            raise ValueError("Vectors must be of the same size")

        result = []
        for i in range(len(self._values)):
            result.append(self._values[i] + other._values[i])

        return result

    def __sub__(self, other):
        """
        Operator odejmowania dwóch wektorów
        :param other:
        :return:
        """
        if len(self._values) != len(other._values):
            raise ValueError("Vectors must be of the same size")

        result = []
        for i in range(len(self._values)):
            result.append(self._values[i] - other._values[i])

        return result



    def __mul__(self, scalar):
        """
        Funkcja mnoży wektor przez skalar
        :param scalar: liczba (float)
        :return: wektor pomnożony
        """
        return Vector(x * scalar for x in self._values)

    def scalar_multiply(self, scalar):
        """
        Funkcja mnoży skalar przez wektor
        :param scalar: liczba (float)
        :return: wektor pomnożony
        """
        return Vector(x * scalar for x in self._values)

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
    # test konstruktora
    v1 = Vector()
    print(str(v1))
    v2 = Vector(3)
    print(str(v2))

    # test losowej generacji elementów wektora
    v1.randomize()
    print(v1)

    # test wczytywania elementów wektora z listy
    v2.read_values([8,2,7])
    print((v2)) #tu cos nie dziala

    # test operatora dodawania dwóch wektorów
    v3 = v1 + v2
    print(str(v3))

    # test operatora odejmowania dwóch wektorów
    v4 = v1 - v2
    print(str(
        v4))
    # test mnożenia wektora przez skalar
    v5 = v1 * 2
    print(str(v5))

    # test wyliczania długości wektora
    print((v1.length()))
    print(abs(v2.length()))

    # test wyliczania sumy elementów wektora
    print(v1.sum())

    # test wyliczania iloczynu skalarnego dwóch wektorów
    print(abs(v1.dot_product(v2)))

    # test operatora []
    print(v1[0])

    # test operatora in
    print(0.5 in v1)
    print(2.5 not in v1)


