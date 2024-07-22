## operasi

# index  0(-3)   1(-2)   3(-1)
data = ['Ucup','Otong','Dudung']

# mengambil data dari list
data_0 = data[0]
print(f'data pertama (index 0) = {data_0}')

data_last = data[-1]
print(f'data terakhir adalah = {data_last}')

data_ucup = data[-3]
print(f'data ucup = {data_ucup}')

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'panjang data = {panjang_data}')

# manipulasi data list

# menambah item pada list sesuai posisi
print(f'\ndata sebelum ditambah: \n{data}')

data.insert(1,'Asep')
print(f'\ndata sesudah ditambah: \n{data}')

# menambah di akhir list
data.append('Jajang')
print(f'\ndata sesudah ditambah: \n{data}')

# menambah list dengan list
data_baru = ['Ujang','Usep','Dadang']
data.extend(data_baru)
print(f'\ndata gabungan: \n{data}')

# meremove data
data.remove('Ujang')
print(f'\ndata remove: \n{data}')
# data.remove('usep) , akan error karena huruf harus sesuai ('Usep)

# meremove data paling belakang
data.pop()
print(f'\ndata akhir: \n{data}')