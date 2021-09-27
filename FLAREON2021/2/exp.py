magic = [0x89,  0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]
encrypted = [0xc7, 0xc7, 0x25, 0x1d, 0x63, 0x0d, 0xf3, 0x56]


key = [0x3, ]

def rol(n, d):

    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d)|(n >> (32 - d))

# Function to right
# rotate n by d bits
def ror(n, d):

    # In n>>d, first d bits are 0.
    # To put last 3 bits of at
    # first, do bitwise or of n>>d
    # with n <<(INT_BITS - d)
    return (n >> d)|(n << (32 - d)) & 0xFFFFFFFF


a = 0xc7 ^ ord('o')
print(bin(a)[2:])
a = rol(a, 1)
print(hex(a))

'''
for i in range(8):
    magic[i]+i
'''
