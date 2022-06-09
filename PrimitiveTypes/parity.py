# time complexity is o(n), and n represents the length of the bits eg: 12(int) / 0b1100 is 4.
def parity(x: int) -> int:
    result = 0
    while x:
        # 0b0101
        # the ^= is an XOR operator. It means set the result to 1 if result is not the same as z & 1, otherwise
        # set to zero.
        result ^= x & 1
        x >>= 1
    return result


# odd number of ones so parity is 1
print("Parity: " + str(parity(int('0b10010001', 2))))

# even number of ones so parity is 0
print("Parity: " + str(parity(int('0b10000001', 2))))

# we can improve performance by using this bit-fiddling trick x & (x - 1)
# https://youtu.be/C5EkxfNEMjE?t=742 (subtraction to understand)
# x = 0b00101100
# 1 = 0b00000001

# when borrowing we replace the zero with a two, if borrow from a 2 we replace with a 1.
# 0b00101012
# 0b00000001
# ----------
# 0b00101011

# x & (x - 1)
# 0b00101100 & (0b00101011)

# 0b00101100
# 0b00101011
# ----------
# 0b00101000

# with this we have removed the lowest set bit within a binary number e.g. 0b00101100 becomes 0b00101000. This means we
# can set the time complexity to k = number of set bits. We will just loop through the binary numbers of set bits only.
# e.g. 0b00101100 would have a time complexity of 3.
