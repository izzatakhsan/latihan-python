# latihan

#kalkulator sederhana
print(10*'=')
print('Kalkulator Sederhana')
print(10*'=' + '\n')

angka1 = float(input('Masukkan angka pertama: '))
operator = input('Operatorn (+,-,x,/): ')
angka2 = float(input('Masukkan angka kedua: '))

# percabangannya

if operator == '+':
    hasil = angka1 + angka2
    print(f'Hasilnya adalah = {hasil}')
elif operator == '-':
    hasil = angka1 - angka2
    print(f'Hasilnya adalah = {hasil}')
elif operator == 'x':
    hasil = angka1 * angka2
    print(f'Hasilnya adalah = {hasil}')
elif operator == '/':
    hasil = angka1 / angka2
    print(f'Hasilnya adalah = {hasil}')
else:
    print('Operator yang Anda masukkan salah!')
    print('Masukin yang bener dong!!!')