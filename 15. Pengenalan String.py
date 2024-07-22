data = 'ini adalah string'
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hello World!"')
print("'Hello World!'")
print("Ini adalah hari Jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day mate, isn\'t it?')

# backslash
print("C:\\User\\Ucup")

# tab
print("ucup\totong, jadi jauhan")

# backspace
print("ucup  \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.")   # LF = line feed (unix, macos, linux)
print("baris pertama.\rbaris kedua.")   # CR = carriage return (commodore, acorn, lisp)
print("baris pertama.\r\nbaris kedua.") # CRLF = line feed carriage return (windows)

# 3. string literal atau raw

# raw
print(r'C:\new folder')

# literal string
print("""
Nama: Ucup
Kelas: 4 SMA      
""")

# multiline literal string dan raw
print(r"""
Nama: Ucup
Kelas: 4 SMA\new
Website: www.ucup.com/newID
""")