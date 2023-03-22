import random

class Vector:
    """
    Klasa Vector przechowująca kolekcję liczb.
    """

    def __init__(self, size=3):
        """
        Funkcja określa wielkosc wektora
        :param size:(int) rozmiar wektora(domyślnie będzie 3)
        """
        self._values = [0] * size

    def generator(self):
        """
        Funkcja losowo generuje elementy wektora
        :return: wektor o losowych elementach(float)
        """
        for i in range(len(self._values)):
            self._values[i] = random.random()

    def read_values(self, values):
        """
        Funkcja wczytuje elementy wektora z listy podanej jako argument
        :param values: wartosci wektora(float)
        :return: nowy wektor
        """

        if len(values) != len(self._values):
            raise ValueError("Zły rozmiar wektorów.")
        self._values = values

    def __add__(self, other):
        """
        Funkcja dodaje dwa wektory
        :param other: wektor
        :return: wektor z dodanych wektorów
        """
        if len(self._values) != len(other._values):
            raise ValueError("Wektory muszą być tego samego rozmiaru")

        result = []
        for i in range(len(self._values)):
            result.append(self._values[i] + other._values[i])
        self._values = result
        return self._values

    def __sub__(self, other):
        """
        Funkcja odejmuje dwa wektory
        :param other: wektory
        :return: wektor-różnica wektorów
        """
        if len(self._values) != len(other._values):
            raise ValueError("Wektory muszą być tego samego rozmiaru")

        result = []
        for i in range(len(self._values)):
            result.append(self._values[i] - other._values[i])
        self._values = result
        return self._values

    def __mul__(self, scalar):
        """
        Funkcja mnoży wektor przez skalar
        :param scalar: liczba (float)
        :return: wektor pomnożony
        """

        result = []
        for i in range(len(self._values)):
            result.append(self._values[i] * scalar)
        self._values = result
        return self._values


    def mnozenieskalar(self, scalar):
        """
        Funkcja mnoży skalar przez wektor
        :param scalar: liczba (float)
        :return: wektor pomnożony
        """

        result = []
        for i in range(len(self._values)):
            result.append(self._values[i] * scalar)
            #result.append([x * scalar for x in self._values])
        self._values = result
        return self._values

    def length(self):
        """
        Funkcja liczy dlugość wektora
        :return: dlugosc wektora
        """

        return (sum(x ** 2 for x in self._values)) ** 0.5

    def sum(self):
        """
        Funkcja wylicza sume elementów wektora
        :return: suma elementów(float)
        """

        return sum(self._values)

    def iloczyn_skalarny(self, other):
        """
        Funkcja wylicza iloczyn skalarny dwóch wektorów
        :param other: drugi wektor
        :return: iloczyn(float)
        """

        if len(self._values) != len(other._values):
            raise ValueError("Zły rozmiar wektorów.")
        return sum(self._values[i] * other._values[i] for i in range(len(self._values)))

    def __str__(self):
        """
        reprezientacja tekstowa wektora
        :return: wektor
        """

        return f"Vector({self._values})"

    def __getitem__(self, index):
        """
        Funkcja pozwala na dostęp do konkretnych elementów wektora
        :param index: numer elementu wektora(int)
        :return: element wektora(float)
        """

        return self._values[index]

    def __contains__(self, item):
        """
        Funkcja sprawdza przynaeznosc elementu do wektora
        :param item:element
        :return: true/false
        """

        return item in self._values


