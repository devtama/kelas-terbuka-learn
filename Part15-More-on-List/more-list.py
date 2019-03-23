Barang = ['buku','gelas','kopi','laptop','hedset']
print(Barang)

# Beberapa method untuk memanipulasi list

# Menambah data
Barang.append("dompet") # Untuk menambah
print(Barang)

Barang.extend("HP") # ini mengambil iterable
print(Barang)

Barang.insert(2,"teh") # menambah ke baris tertentu
print(Barang)

# menghitung anggota
jumlahBarang = Barang.count('kopi')
print(f"jumlah kopi dimeja piscki adalah {jumlahBarang}")

# meremove data
Barang.remove('hedset')
print(Barang)

Barang.reverse()
print(Barang)

Stuff = Barang.copy()
Stuff.append('printer')
print(Stuff)
print(Barang)