from lista1zadanie1 import *
print('test konstruktora')
v1 = Vector()
print(str(v1))
v2 = Vector(3)
print(str(v2))

print('test losowej generacji elementów wektora')
v1.generator()
print(v1)

print('test wczytywania elementów wektora z listy')
v1.read_values([4, 5, 6])
print(v1)
v2.read_values([1, 2, 3])
print(v2)

print('test dodawania')
v1 + v2
print(str(v1))

print('test  odejmowania')
v1 - v2
print(str(v1))

print('test mnożenia wektora przez skalar')
v1 * 2
print(v1)
print(v1.mnozenieskalar(2))

print('test wyliczania długości wektora')
print(v1.length())
print(v2.length())

print('test wyliczania sumy elementów wektora')
print(v1.sum())

print('test wyliczania iloczynu skalarnego dwóch wektorów')
print(v1.iloczyn_skalarny(v2))

print('test operatora []')
print(v1[1])

print('test operatora in')
print(16 in v1)
print(2 not in v2)
