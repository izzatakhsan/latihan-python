# format string

# contoh generik
nama = 'ucup'
format_str = f'hello {nama}'
print(format_str)

# bool
boolean = False
format_str = f'bool = {boolean}'
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f'bil. bulat = {angka:d}'
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f'bil. bulat = {angka:,}'
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:09.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f'minus = {angka_minus:+d}'
format_plus = f'plus = {angka_plus:+.2f}'
print(format_minus)
print(format_plus)

# memformat persen
persen = 0.045
format_persen = f'persen = {persen:.2%}'
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_str = f'harga total = Rp. {harga*jumlah:,}'
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 225
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)