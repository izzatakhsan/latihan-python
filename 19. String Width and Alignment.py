# width and multiline

# data
nama = "Ucup Surucup"
umur = 17
tinggi = 150.1
sepatu = 44

# string standard
data_string = f'nama = {nama}, umur = {umur}, tinggi = {tinggi}, ukuran sepatu = {sepatu}'
print(5*'='+'Data String'+5*'=')
print(data_string)

# string multiline (enter, newline, \n)
data_string = f'nama = {nama} \numur = {umur} \ntinggi = {tinggi} \nukuran sepatu = {sepatu}'
print('\n'+5*'='+'Data String'+5*'=')
print(data_string)

# string multiline (kutip trplets)
data_string = f'''nama = {nama}
umur = {umur}
tinggi = {tinggi}
ukuran sepatu = {sepatu}
'''
print('\n'+5*'='+'Data String'+5*'=')
print(data_string)

# mengatur lebar
nama = 'Ucup'
data_string = f'''
nama          = {nama:>5}
umur          = {umur:>5}
tinggi        = {tinggi:>5}
ukuran sepatu = {sepatu:>5}
'''
print('\n'+5*'='+'Data String'+5*'=')
print(data_string)