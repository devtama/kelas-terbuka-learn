#else, break, continue, pass

angka = 0

while angka < 15:

    if angka is 5:
        # print('check1')
        # angka += 1
        continue
        # print('check2')
    print("nilai angka adalah", angka)
    angka += 1
else:
    print('nilai angka diakhir while adalah', angka)

print('outside')