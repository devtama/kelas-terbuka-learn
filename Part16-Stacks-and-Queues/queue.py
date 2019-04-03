# Belajar Queue
# secara default queue tidak built in jadi harus import module

from collections import deque

antrian = deque([1,3,5,7,9])

print(f"data sekarang adalah {antrian}")

# Menambah data

antrian.append(11)
print(f"data masuk {11}")
print(f"data sekarang adalah {antrian}")

antrian.append(13)
print(f"data masuk {13}")
print(f"data sekarang adalah {antrian}")

# Mengurangi antrian
out = antrian.popleft() # untuk menghapus antrian didepan
print(f"data keluar {out}")
print(f"data sekarang adalah {antrian}")