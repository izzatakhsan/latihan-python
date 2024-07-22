# latihan perulangan membuat segitiga

sisi = 10

# 1. menggunakan for

# dummy variable
count = 1

for i in range(sisi):
    print('*'*count)
    count += 1

print('akhir dari for\n')

# 2. menggunakan while

count = 1
while True:
    print('*'*count)
    count += 1

    if count > sisi:
        break

print('akhir dari while\n')

# 3. hanya ganjil saja

count = 1
while True:
    if count%2:
        # print jika ganjil
        print('*'*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print('akhir dari while\n')

# 4. Segitiga sama kaki

count = 1
spasi = int(sisi / 2)
while True:
    if count%2:
        # print jika ganjil
        print(' '*spasi+'*'*count)
        count += 1
        spasi -= 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print('akhir dari while')