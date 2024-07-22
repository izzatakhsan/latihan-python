''' *args '''

# memasukkan data/argument

def fungsi(nama,tinggi,berat):
    print(f'{nama} punya tinggi {tinggi}cm dan berat {berat}kg')

fungsi('Ucup',170,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} punya tinggi {tinggi}cm dan berat {berat}kg')

fungsi(['Otong',100,120])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} punya tinggi {tinggi}cm dan berat {berat}kg')

fungsi('Dudung',120,100)

# studi kasus

def tambah(*data):
    # data tipenya tuple, bisa diiterasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f'hasil = {hasil}')

hasil = tambah(10,20,30)
print(f'hasil = {hasil}')