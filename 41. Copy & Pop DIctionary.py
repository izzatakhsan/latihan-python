# copy dictionary

teman2 = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung',
    'sep':'asep si kasep',
    'cuy':'ucuy surucuy'
}

friends = teman2.copy()

print(f'teman2: {teman2}\n')
print(f'friends: {friends}\n')

teman2['cup'] = 'ucup si kewren'
print(f'teman2: {teman2}\n')
print(f'friends: {friends}\n')

# pop disctionary (berdasarkan key)
dataAsep = friends.pop('sep')
print(f'data asep: {dataAsep}\n')
print(f'friends: {friends}\n')

# popitem disctionary (yg terakhir doang)
dataTerakhir = friends.popitem()
print(f'data terakhir: {dataTerakhir}\n')
print(f'friends: {friends}\n')