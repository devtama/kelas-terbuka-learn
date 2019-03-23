# Program konversi cm ke meter
def cmtom(argumen):
    print("anda memasukan", argumen, "cm")
    m = argumen / 100
    print("sehingga", argumen, "cm adalah", m, "m")
    return m

# Program konversi meter ke cm
def mtocm(argumen):
    print("anda memasukan", argumen, "m")
    cm = argumen * 100
    print("sehingga", argumen, "m adalah", cm, "cm")
    return cm

cmtom(9023)
mtocm(89.29)