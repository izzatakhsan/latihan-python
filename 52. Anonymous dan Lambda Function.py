# lambda function

def f_kuadrat(angka):
    return angka**2

print(f'hasil fungsi f_kuadrat = {f_kuadrat(3)}')

# lambda
# output = lambda argument: expression
kuadrat = lambda angka: angka**2
print(f'hasil lambda kuadrat = {kuadrat(4)}')

pangkat = lambda num,pow: num**pow
print(f'hasil lambda pangkat = {pangkat(2,3)}')

# sorting untuk list biasa
data_list = ['Otong','Ucup','Dudung']
data_list.sort()
print(f'\nsorted list = {data_list}')

# sorting panjang data
# pakai fungsi
def panjang(nama):
    return len(nama)

data_list.sort(key=panjang)
print(f'\nsorted list by panjang = {data_list}')

# pakai lambda
data_list = ['Otong','Ucup','Dudung']
data_list.sort(key= lambda nama: len(nama))
print(f'\nsorted list by lambda = {data_list}')

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_lambda = list(filter(lambda x: x < 5,data_angka))

print(f'\n<5: {data_angka_baru}')
print(f'<5: {data_angka_lambda}')
print('\n')

# kasus genap
data_genap = list(filter(lambda x: (x%2==0), data_angka))
print(f'genap: {data_genap}')

# kasus ganjil
data_ganjil = list(filter(lambda x: (x%2!=0), data_angka))
print(f'ganjil: {data_ganjil}')

# kasus ganjil
data_3 = list(filter(lambda x: (x%3==0), data_angka))
print(f'kelipatan 3: {data_3}')

# anonymous function
# currying <- haskell curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f'fungsi biasa = {data_hasil}')

# dengan currying menjadi
def pangkat(n):
    return lambda angka: angka**n

pangkat2 = pangkat(2)
print(f'pangkat 2 = {pangkat2(5)}')
pangkat3 = pangkat(3)
print(f'pangkat 3 = {pangkat3(3)}')
print(f'pangkat bebas = {pangkat(4)(5)}')