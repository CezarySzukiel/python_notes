def byte_at(v, n):
    """extracting bytes with shifts"""
    s = n * 8
    return (v & 0xff) << s


print(hex(byte_at(0xdc143c, 0))) # 0x3c
print(hex(byte_at(0xdc143c, 1))) # 0x14


crimson = 0xdc143c0

def rgb(color):
    return (
        byte_at(color, 2),
        byte_at(color, 1),
        byte_at(color, 0)
    )




print(rgb(crimson)) # (220, 20, 60)


def invert_bits(x, num_bits):
    if x < 0:
        raise ValueError('cannot invert negative bits')
    complement = ~x
    inverted = complement + (1 << num_bits)
    if inverted < 0:
        raise ValueError(f'cannot invert {x} in {num_bits} bits')
    return inverted


# print(invert_bits(-23, 8)) # ValueError: cannot invert negative bits
# print(invert_bits(0b1111, 3))  # ValueError: cannot invert 15 in 3 bits
print(bin(invert_bits(0b00110011, 8)))
