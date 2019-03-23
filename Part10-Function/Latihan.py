# Latihan Function di Python
# Script written by Piscki Tama

def volumeBalok(p,l,t): 
    vol =  p * l * t
    print("panjang balok adalah", p)
    print("lebar balok adalah", l)
    print("tinggi balok adalah", t)
    print(f"sehingga Volume balok adalah {p} x {l} x {t} = {vol}")

volumeBalok(1,3,4)

print(10*'=')

def volumeKubus(s):
    v = s**3
    print("sisi kubus adalah",s)
    print(f"sehingga volume kubus adalah {s} x {s} x {s} = {v}")

volumeKubus(5)