# If yang berulang
nilai1 = 75
nilai2 = 80

if nilai1 == 75:
    print("nilai anda:",nilai1)
    print("step 1")
    if nilai2 == 80:
        print("nilai anda:",nilai2)
        print("step 2")

nilai = 50

if nilai == 75:
    print("nilai anda:",nilai)

if nilai is 60:
    print("nilai anda:",nilai)

if nilai is not 60:
    print("nilai anda bukan 60")

print(20*"=")
nilai = 9

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai <= 80:
    print("nilai anda adalah B")
elif 60 <= nilai <= 70:
    print("nilai anda adalah C")
elif 50 <= nilai <= 60:
    print("nilai anda adalah T, lakukan perbaikan")
else:
    print("TIDAK LULUS!")

print(20*"=")

print("operator logika untuk list dan string")
print(" ")

gorengan = ["bakwan","cireng","bala-bala","gehu","combro","pukis"]
beli = "buku"

if beli in gorengan:
    print('Mamang bilang,"ya saya jual',beli,'"')

if not beli in gorengan:
    print('Mamang bilang,"ya saya ga jual',beli,'"')

karakter = "u"
if karakter in beli:
    print("ada", karakter, "di", beli)
else:
    print("tidak ada", karakter, "di", beli)