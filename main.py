a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")

p = 0
l = 0

while int(a) > 0:
    liczba_a = int(a) % 10
    liczba_b = int(b) % 10

    suma = liczba_a + liczba_b + p

    if suma >= 10:
        l += 1
        p = 1
    else:
        p = 0

    a = int(a) / 10
    b = int(b) / 10

print(l)