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

print("*** Selamat datang di Program Konversi CM ke M, dan sebaliknya ***")
print("Pertama silahkan pilih mana yang akan Anda inginkan\n1. cm to m\n2. m to cm")
pilihan = int(input("masukkan pilihan anda: "))

if pilihan == 1:
    cm = int(input("silahkan masukkan angka di cm:"))
    cmtom(cm)
elif pilihan == 2:
    m = int(input("silahkan masukkan angka di cm:"))
    mtocm(m)
else:
    print("pilihan tidak ditemukan!")