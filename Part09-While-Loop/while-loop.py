# BElajar While
# Selama argument true maka akan terus berjalan


## Cara 1
angka = 0

while angka < 5:
    print("nilai angka adalah", angka)
    angka = angka + 1

print("outside")


## Cara 2 dengan Boolean
start = True
angka = 0

while start:
    print("ini didalam while")
    if angka is 100:
        start = False
        print("oke angka 100 ditemukan")
    angka+= 1