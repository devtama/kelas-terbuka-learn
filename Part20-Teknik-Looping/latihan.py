## Menggunakan enumerate
klub = ['Persib','Persija','Persebaya']

for i,klub_bola in enumerate(klub):
    print(f"{i+1}. {klub_bola}")

print("")
## Zip
negara = ['Indonesia', 'Malaysia', 'Brunei Darussalam', 'Thailand', 'Vietnam']
ibukota = ['Jakarta', 'Kuala Lumpur', 'Bandar Seri Bengawan', 'Bangkok', 'Ho Chi Min City']

for k,l in zip(negara,ibukota):
    print(f"Negara {k} ibukotanya {l}")

print("")
## set
jabar = {'tasik','ciamis','banjar','bogor','garut','sumedang','bekasi','depok','cianjur','sukabumi','bandung','majalengka','cirebon','subang','purwakarta','indramayu','kuningan','karawang'}
for j in sorted(jabar):
    print(j)

print("")

## dictionary
bandung_raya = {
    "Kota Bandung" : "Bandung",
    "Kabupaten Bandung" : "Soreang",
    "Kabupaten Bandung barat" : "Padalarang",
    "Kota Cimahi" : "Cimahi"
}

for x,y in bandung_raya.items():
    print(f"Wilayah {x} ibukotanya adalah {y}")

print("")

## Reverse Data (Dibalik)
for i in reversed(range(1,21,1)):
    print(i)