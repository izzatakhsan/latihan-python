# latihan fungsi

import os

# # program luas & keliling persegi panjang
#
# # membuat header program
# os.system('cls')
#
# print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
# print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
# print(f'{'-'*40:^40}')
#
# # mengambil input dari user
# PANJANG = int(input('Masukkan nilai panjang: '))
# LEBAR = int(input('Masukkan nilai lebar: '))
#
# # program menghitung luas & keliling
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)
#
# # menampilkan hasil
# print(f'\nLuasnya adalah {LUAS}')
# print(f'Kelilingnya adalah {KELILING}')

def header():
    os.system('cls')
    print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
    print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
    print(f'{'-'*40:^40}')

def input_user():
    panjang = int(input('Masukkan nilai panjang: '))
    lebar = int(input('Masukkan nilai lebar: '))
    return panjang,lebar

def hitung_luas(panjang,lebar):
    return panjang*lebar

def hitung_keliling(panjang,lebar):
    return 2*(panjang+lebar)

def display(message,value):
    print(f'Hasil perhitungan {message} = {value}')

while True:
    header()
    PANJANG,LEBAR = input_user()
    LUAS = hitung_luas(PANJANG,LEBAR)
    KELILING = hitung_keliling(PANJANG,LEBAR)

    display('luas', LUAS)
    display('keliling', KELILING)

    isContinue = input('\nApakah lanjut (y/n)? ')
    if isContinue =='n':
        break

print('\nProgram selesai.')