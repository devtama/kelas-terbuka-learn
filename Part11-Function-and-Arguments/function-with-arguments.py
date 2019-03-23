# Fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print("siswa ini bernama:",nama)

siswa("piscki")

# fungsi dengan keywords arguments
def guru(nama,pelajaran):
    print("Guru ini bernama",nama)
    print("Mengajar",pelajaran)

guru("Piscki","Pemrograman Dasar")
print(10*"=")
guru(pelajaran='olahraga',nama='heri')
print(10*"=")

# Fungsi dengan menggunakan default argument
def penjangaSekolah(nama,shift='siang',galak='tidak'):
    print('penjaga ini bernama',nama)
    print('shiftnya', shift)
    print('Galak?',galak)

penjangaSekolah("idoy")
penjangaSekolah("ujeng",shift='malam')
penjangaSekolah("usep",galak='sangat')
