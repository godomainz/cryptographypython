def xor(x, s):
    print('----------------------------------------')
    print(x, ' xor ', s, ' = ', x ^ s)
    print(bin(x)[2:].zfill(8), ' xor ', bin(s)[2:].zfill(8), ' = ', bin(x ^ s)[2:].zfill(8))
    print('----------------------------------------')


xor(4, 8)
xor(4, 4)
xor(255, 1)
xor(255, 128)
