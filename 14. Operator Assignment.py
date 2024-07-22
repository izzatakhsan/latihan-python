a = 5  # assignment
print('nilai a =', a)

a += 1  # a = a + 1
print('a += 1, nilai a =', a)

a -= 2  # a = a - 2
print('a -= 2, nilai a =', a)

a *= 5  # a = a * 5
print('a *= 5, nilai a =', a)

a /= 2  # a = a / 2
print('a /= 2, nilai a =', a)

a %= 3  # a = a % 3
print('a %= 1, nilai a =', a)

a = 10
print('\nnilai a =', a)
a //= 3  # a = a // 3
print('a //= 3, nilai a =', a)

b = 5
print('\nnilai b =', b)
b **= 3 # b = b ** 3
print('b **= 3, nilai b =', b)

# OR
c = True
print('\nnilai c =', c)
c |= False
print('c |= False, nilai c =', c)
c = False
print('nilai c =', c)
c |= False
print('c |= False, nilai c =', c)

# AND
c = True
print('\nnilai c =', c)
c &= False
print('c &= False, nilai c =', c)
c = True
print('nilai c =', c)
c &= True
print('c &= True, nilai c =', c)

# XOR
c = True
print('\nnilai c =', c)
c ^= False
print('c ^= False, nilai c =', c)
c = True
print('nilai c =', c)
c ^= True
print('c ^= True, nilai c =', c)

# geser-geser
d = 0b0100
print('\nnilai d =', format(d, '04b'))
d >>= 2
print('nilai d >>= 2, nilai d =', format(d, '04b'))
d <<= 1
print('nilai d <<= 1, nilai d =', format(d, '04b'))