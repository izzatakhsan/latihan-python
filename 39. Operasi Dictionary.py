# operator dictionary

data_dict = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung'
}

# panjang dictionary
LENDICT = len(data_dict)
print(f'panjang dictionary: {LENDICT}')

# mengecek key exist or not
KEY = 'cup'
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data_dict: {CHECKKEY}')

# mengakses value (read) dengan get
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('kis','key tidak ditemukan')) # cek key dengan message

# mengupdate data
data_dict['cup'] = 'ucup si ganteng'
print(data_dict)
data_dict['sep'] = 'asep si kasep'
print(data_dict)

data_dict.update({'cup':'ucup surucup'})
print(data_dict)
data_dict.update({'izt':'izzat si kull'}) # kalau tidak ada key nya -> add key baru
print(data_dict)

#delete data pada dictionary
del data_dict['izt']
print(data_dict)