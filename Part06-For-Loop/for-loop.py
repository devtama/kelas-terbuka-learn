gorengan = ['bakwan','cireng','gehu','combro','tempe']

for g in gorengan:
    print(g)
    print(len(g))

# String sebagai iterabel

food = 'nasi goreng'

for i in food:
    print(i)

# for di dalam for
print(20*'=')

buah = ['semangka','jeruk','apel','anggur']
junk = ['burger','kfc','hotdog','pizza']

daftar = [gorengan, buah,junk]
for subdaftar in daftar:
    print(subdaftar)
    for komponen in subdaftar:
        print(komponen)