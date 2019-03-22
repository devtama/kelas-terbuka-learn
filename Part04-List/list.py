Data = [1,4,9,16,25,36,49,64]

# Mengakses List
Subdata1 = Data[3]
Subdata2 = Data[-3]

# Memotong List
Subdata3 = Data[2:4]
Subdata4 = Data[:4]

Data2 = [100,200,300,400,500,600,700,800]

# Menambah List
Data3 = Data+Data2

# Merubah konten dari List

#Data[4] = 87

# Mengvopy Lust ke variable baru
a = Data[:]
a[7] = 87

# Merubah content list dengan menggunakan metode sliceing
Data[3:5] = [11,12]

# List dalam list
x = [Data,Data2]

# Mengakses list dalam multidimension list
y = x[1][4]

# Method untuk list
Data.append(30)

# Function yang bisa kita  gunakan kepada list
panjang_list = len(Data)

print(Data)
print(panjang_list)