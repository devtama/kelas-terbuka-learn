# Latihan Scope Global

kesukaan = "javascript"
framework = "nodejs"

def ubahKesukaan(new):
    global kesukaan
    kesukaan = new
    print("saya ubah kesukaan saya menjadi", kesukaan)

ubahKesukaan("php")

print(40*"=")

def pasangan(bahasa,frame):
    global kesukaan, framework
    kesukaan = bahasa
    framework = frame

pasangan('python','django')
print("pemrograman", kesukaan,"mempunyai",framework)

print(40*"=")

aku = 'tama'
dia = 'rahma'

def jodoh(cowo,cewe):
    global aku, dia
    aku = cowo
    dia = cewe


jodoh("Piscki","Fenti")
print(aku,"akan menikahi",dia,"di tahun 2024")