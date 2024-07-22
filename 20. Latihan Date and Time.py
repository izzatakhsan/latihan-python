# date and time

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f'hari ini adalah hari: {hari_ini:%A}')

tanggal = dt.date(2005,10,10)
print(tanggal)

print('Apa hari lahir Anda?')
print('Silahkan masukkan tanggal, bulan, dan tahun Anda lahir.')
tanggal = int(input('Tanggal\t: '))
bulan = int(input('Bulan\t: '))
tahun = int(input('Tahun\t: '))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'Hari Anda lahir adalah: {tanggal_lahir:%A}')

print(f'Tanggal lahir Anda: {tanggal_lahir}')
print(f'Hari ini tanggal: {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f'Umur Anda sekarang adalah: {umur_tahun} tahun {umur_bulan} bulan')