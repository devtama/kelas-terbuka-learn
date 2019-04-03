## Belajar Set
# Set itu adalah himpunan
# Karakteristik himpunan tidak punya urutan
# Set tidak support indexing

## cara 1
hero = {"spiderman",
        "Wiro Sableng",
        "batman",
        "Gundala",
        "Gatot kaca"}

hero.add("super dede")
print(hero)

print("")

## Cara 2
superhero = set()

superhero.add("batman")
superhero.add("antman")
superhero.add("superman")
superhero.add("spiderman")
superhero.add(212)

print(superhero)

print("")

## Contoh
ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7,11}

print(f"Gabungan dari himpunan bilangan {ganjil} dan {genap} adalah: {ganjil.union(genap)}") # Gabungan
print(f"Irisan dari himpunan bilangan {ganjil} dan {prima} adalah: {ganjil.intersection(prima)}") # irisan