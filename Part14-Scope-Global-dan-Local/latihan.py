# Latihan Scope Global

kesukaan = "javascript"
framework = "nodejs"

def ubahKesukaan(new):
    global kesukaan
    kesukaan = new
    print("saya ubah kesukaan saya menjadi", kesukaan)

ubahKesukaan("python")

print("")

def pasangan(bahasa,frame):
    global kesukaan, framework
    kesukaan = bahasa
    framework = frame

pasangan('python','django')
print("pemrograman", kesukaan,"mempunyai framework",framework)

print("")

aku = 'tama'
dia = 'rahma'

def jodoh(cowo,cewe):
    global aku, dia
    aku = cowo
    dia = cewe


jodoh("Piscki","Fenti")
print(aku,"akan menikahi",dia,"di tahun 2024")

print("")

klub = "Persikab"
stadion = "Si Jalak Harupat"

def fc(klub1, stadion1):
    global klub, stadion
    klub = klub1
    stadion = stadion1

fc("Persib","Siliwagi")
print(f"Dulu {klub} bermarkas di stadion {stadion}, sekarang di {stadion}")