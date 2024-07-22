# fungsi dengan kembalian

# fungsi kuadrat
def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah
def plus(angka_1,angka_2):
    return angka_1 + angka_2

a = plus(10,5)
print(a)

# fungsi dengan return banyak
def operasi_mtk(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,kali,bagi

k,l,m,n = operasi_mtk(3,2)
print(f'Hasil tambah = {k}')
print(f'Hasil kurang = {l}')
print(f'Hasil kali = {m}')
print(f'Hasil bagi = {n}')