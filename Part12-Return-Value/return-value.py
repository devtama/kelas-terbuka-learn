# Fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print("nilai kuadrat dari",argumen,"adalah",total)
    return total

a = kuadrat(12)
print(a)

print(15*"=")

# Fungsi dengan return value dan multiple argumen
def tambah(argumen1, argumen2):
    total = argumen1 + argumen2
    print(argumen1, '+', argumen2,'=',total)
    return total

def kali(argumen1, argumen2):
    total = argumen1 * argumen2
    print(argumen1, 'x', argumen2,'=',total)
    return total

a = tambah(2,3)
b = kali(4,tambah(7,3))
print(b)
