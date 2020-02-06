import math

def num_bits(n):
    if n == 0: return 0
    res = 0
    max_bit = int(math.log(n, 2)) + 1
    for i in range(max_bit):
        if n & 1: res += 1
        n >>= 1
    return res


def test():
    for h in range(12):
        res = num_bits(h)
        print(f"{h}: number of bits -> {res}")

    for m in range(60):
        res = num_bits(m)
        print(f"{m}: number of bits -> {res}")


if __name__ == '__main__':
    test()

