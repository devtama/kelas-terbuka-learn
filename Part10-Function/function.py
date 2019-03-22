# Belajar Fungsi

# Cara mendefinisikan fungsi
def fungsi():
    print("Belajar Fungsi")

# Memanggil fungsi
fungsi()

# contoh fungsi sederhana
def suaraAyam():
    print("kukuruyuk")

def hargaAyam():
    suaraAyam()
    print('harga ayam mahal')

# membuat fungsi dengan input argumen
def hargaTotalAyam(kg):
    suaraAyam()
    harga = 20000
    hargaTotal = kg*harga
    print('harga',kg,'ayam adalah', hargaTotal)

hargaAyam()
hargaTotalAyam(2)
hargaTotalAyam(0.1)