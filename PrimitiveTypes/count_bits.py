# time complexity is o(n), and n represents the length of the bits eg: 12(int) / 0b1100 is 4.
def count_bits(x: int) -> int:
    num_bits = 0
    # while x has a number greater than zero.
    while x:
        # This is checking if two values are set because 1 will only have 1 set bit we can compare it directly.
        # 0b10010001
        # 0b00000001
        num_bits += x & 1

        # shift the bit off the end eg
        # 0b10010001, 0b1001000, 0b100100, 0b10010, 0b1001
        x >>= 1
    return num_bits


print(count_bits(int('0b10010001', 2)))
