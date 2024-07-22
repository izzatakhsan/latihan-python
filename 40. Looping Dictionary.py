# looping dictionary

teman2 = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung',
    'sep':'asep si kasep',
    'cuy':'ucuy surucuy'
}

# looping (keluar key doang)
for teman in teman2:
    print(teman)
print('\n')
# operator untuk mengambil item / iterables
keys = teman2.keys()
print(keys)
print('\n')

for key in teman2.keys():
    print(teman2.get(key))
print('\n')

values = teman2.values()
print(values)
print('\n')

for value in teman2.values():
    print(value)
print('\n')

items = teman2.items()
print(items)
print('\n')

for key,value in teman2.items():
    print(f'key = {key}, value = {value}')