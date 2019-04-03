# Teknik Looping

nama_team = ["Budi",
             "Maulana",
             "Wira",
             "Piscki",
             "Ghani",
             "Febrian"] # Harus iterables kalo tidak, tidak akan ditampilkan

alamat = ['Cibolerang',
          'Pasir Koja',
          'Cimenyan',
          'Sayati',
          'Cimahi',
          'Cimaung']

# print("Team Support NoLimit:")
# iterasi = 1
# for team in nama_team:
#     print(f"{iterasi}. {team}")
#     iterasi+=1

## Menggunakan enumerate
print("Anggota Team Technical Support NoLimit: ")
for i,team in enumerate(nama_team):
    print(f"{i+1}. {team}")

print("")

## Zip
for team,tinggal in zip(nama_team, alamat):
    print(f"{team} tinggal di {tinggal}")

print("")

## set and sorted
divisi = {'analyst','platform','marketing','designer','validator','support'}

for aha in sorted(divisi):
    print(aha)

print("")

## dictionary
perdivisi = {
    "Budi" : "head of support",
    "Thema" : "head of analyst",
    "Naurah" : "head of validator"
}

for c,v in perdivisi.items():
    print(f"{c} jabatannya di NoLimit adalah {v}")

print("")

## Reverse Data (Dibalik)
for i in reversed(range(1,10,1)):
    print(i)