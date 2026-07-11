a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")

a = int(a)
b = int(b)

licznik = 0
przekladacz = 0

reversed_a = 0
reversed_b = 0

while a > 0:
    reversed_a = reversed_a * 10 + a % 10
    a //= 10

while b > 0:
    reversed_b = reversed_b * 10 + b % 10
    b //= 10

while reversed_a or reversed_b > 0:
    first_a = reversed_a % 10
    first_b = reversed_b % 10

    suma = first_a + first_b + przekladacz

    if suma >= 10:
        licznik += 1
        przekladacz = 1
    else:
        przekladacz = 0

    reversed_a //= 10
    reversed_b //= 10

    if przekladacz:
        licznik += 1

print(licznik)