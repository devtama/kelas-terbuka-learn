# Exercise Stack and Queues

from collections import deque

# Stack

bahasa = ["python", "js", "php"]
print(f"Bahasa Pemrograman yang harus dikuasai di tahun 2019 {bahasa}")
opsi1 = bahasa.append("golang")

bahasa.pop()
print(f"bahasa pemrograman yang harus dikuasai di 2019 {bahasa}")
bahasa.pop()
print(f"bahasa pemrograman yang WAJIB dikuasai di 2019 {bahasa}")

print ("")

# Queue

capres = deque(["Jokowi", "Prabowo"])
print(f"Kandidat Presiden RI Periode 2019-2024 adalah {capres}")

capres.popleft()
print(f"kandidat paling kuat adalah {capres}")