n = int(input('input angaka: '))
def rek(angka):
    if angka > 0:
        print(angka)
        angka = angka - 1
        rek(angka)
    else:
        print(angka)

rek(n)
