data_angka = [1,3,4,2,4,3,6,8,9,5,3,1,7,0]
print(f'data angka = \n{data_angka}')

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f'jumlah angka 4 = {jumlah_data_4}')
print(f'jumlah angka 3 = {jumlah_data_3}')

# ambil posisi data (index)

data = ['Ucup','Otong','Dudung','Ujang']
print(f'\ndata = {data}')

index_dudung = data.index('Dudung')
index_ujang = data.index('Ujang')
print(f'index si Dudung = {index_dudung}')
print(f'index si Ujang = {index_ujang}\n')

# mengurutkan list
print(f'data belum urut: \n{data_angka}')
data_angka.sort()
print(f'data sudah urut: \n{data_angka}')

print(f'data belum urut: \n{data}')
data.sort()
print(f'data sudah urut: \n{data}')

# membalik list
data_angka.reverse()
data.reverse()
print(f'\ndata reverse: \n{data_angka} \n{data}')
