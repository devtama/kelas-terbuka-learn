# Scope variable Local

namaKucing = "kiki"
makanKucing = "ikan"

def rubahNama(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print("saya rubah nama kucing menjadi",namaKucing)

def kasihMakan(makanan,nama):
    global namaKucing, makanKucing
    namaKucing = nama
    makanKucing = makanan

rubahNama("amel")
kasihMakan('universal','fenti')

print('nama kucing saya menjadi', namaKucing, "dan makan", makanKucing)