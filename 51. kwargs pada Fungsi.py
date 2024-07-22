''' **kwargs '''

def fungsi(nama,tinggi,berat):
    # fungsi biasa
    print(f'{nama} punya tinggi {tinggi}cm dan berat {berat}kg')

fungsi('Ucup',170,60)

def fungsi(**kwargs):
    # fungsi kwargs
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f'{nama} punya tinggi {tinggi}cm dan berat {berat}kg')

fungsi(nama='Ucup',tinggi=170,berat=60)

# studi kasus

def math(*args,**kwargs):
    if kwargs['option'] == 'tambah':
        output = 0
        for angka in args:
            output += angka
    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args:
            output *= angka
    else:
        print('tidak ada operasi')

    return output

hasil = math(1,2,3,4, option='tambah')
print(f'\nhasil jumlah = {hasil}')
hasil = math(1,2,3,4, option='kali')
print(f'hasil kali = {hasil}')