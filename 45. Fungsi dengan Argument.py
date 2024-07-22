# fungsi dengan argument (input)

# program hello
def hello_world(nama):
    print(f'Selamat datang di dunia si {nama}')

hello_world('Ucup')
hello_world('Otong')

# program tambah
def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')

tambah(2,8)
tambah(1000,1)

# program absen
def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'Ada {peserta}')

anggota_girlband = ['Soya','Nini','Mawar','Lilis']

say_hi(anggota_girlband)