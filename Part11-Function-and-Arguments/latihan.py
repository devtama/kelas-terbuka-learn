import math

def luas_lingkaran(title,jari):
    print(title)
    return math.pi * (jari**2)

print(luas_lingkaran("lingkaran 1",10))

def konversiSuhuFtoC(f):
    print("suhu fahrenheit =",f)
    c = 5 * (f - 32) / 9
    print("suhu celsius =",c)

konversiSuhuFtoC(212)