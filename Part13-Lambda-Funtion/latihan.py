import math

luas_lingkaran = lambda j : math.pi * (j**2)

hasil = luas_lingkaran(10)
print(hasil)

print("")

volume_balok = lambda v : v**3

hasil = volume_balok(2)
print(hasil)

print("")

acak = [2, 18, 9, 22, 4,
        17, 24, 8, 12,
        22, 18, 1, 30,
        4, 14, 1, 23,
        51, 8, 31, 13,
        27]

print(filter(lambda x: x > 13 , acak))