# operator dalam bentuk methods
## merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print('normal =', salam)
salam = salam.upper()
print('upper =', salam)

# merubah semua ke lower case
alay = 'aKu KeCe AbieEEzzZZZ'
print('normal =', alay)
alay = alay.lower()
print('lower =', alay)

## pengecekan dengan menggunakan isX method

# contoh untuk pengecekan lower case
salam = 'sist'
is_lower = salam.islower()  # hasilnya bool
print(salam, 'is lower =', str(is_lower))
is_upper = salam.isupper()  # hasilnya bool
print(salam, 'is upper =', str(is_upper))

# isalpha() = huruf
# isalnum() = huruf & angka
# isdecimal() = angka
# isspace() = spasi, tab, newline (\n)
# istitle() = semua kata diawali huruf besar

judul = 'It Is Okay Not To Be Orkay'
cek_judul = judul.istitle() # hasilnya bool
print(judul, 'is title =', str(cek_judul))

judul = "It's Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya bool
print(judul, 'is title =', str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_start = "Sajangnim Oppa".startswith("Sajangnim")
print("start =", str(cek_start))

cek_end = "Sajangnim Oppa".endswith("Oppa")
print("end =", str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
print(pisah)
gabungan = ','.join(pisah)
print(gabungan)
gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = 'akuehmsayangehmkamu'
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
kanan = 'kanan'.rjust(10)
print("'"+kanan+"'")

kiri = 'kiri'.ljust(10)
print("'"+kiri+"'")

tengah = 'tengah'.center(20, ':')
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip(':')
print("'"+tengah+"'")

kanan = kanan.strip()
print("'"+kanan+"'")