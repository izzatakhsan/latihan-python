# list

# kumpulan data angka
data_angka = [1,2,3,4]
print(data_angka)

# kumpulan data string
data_string = ['ucup','otong','odah']
print(data_string)

# kumpulan data boolean
data_bool = [True,False,True]
print(data_bool)

# data campuran
data_campuran = [1,'ucup',True,2.0,'otong',False]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_for = [i**2 for i in range(0,10)]
print(list_for)

# membuat list dengan if
list_for_if = [i**2 for i in range(0,10) if i != 5]
print(list_for_if)

list_for_if = [i**2 for i in range(0,10) if i%2 ==0]
print(list_for_if)

list_for_if = [i**2 for i in range(0,10) if i%2 !=0]
print(list_for_if)