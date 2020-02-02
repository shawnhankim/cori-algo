"""
Convert decimal to base notation

2 <= base <= 10

[Expected Result]
1. res:0000000000000000000000000000000000000000000000000000000000001001 <- num:9, base:2
2. res:0000000000000000000000000000000000000000000000000000000000001000 <- num:8, base:2
3. res:0000000000000000000000000000000001111111111111111111111111111111 <- num:2147483647, base:2
4. res:0111111111111111111111111111111111111111111111111111111111111111 <- num:9223372036854775807, base:2

"""

def convert_from_decimal(num, base):
    res = 0
    i = 0
    while num:
        denominator = num % base
        res += denominator * (10 ** i)
        num //= base
        i += 1
    return res


def convert_from_decimal2(num, base):
    res = 0
    multiplier = 1
    while num:
        res += num % base * multiplier
        num //= base
        multiplier *= 10
    return res

def test():
    test_cases = [
        {"num": 9, "base": 2},
        {"num": 8, "base": 2},
        {"num": 2147483647, "base": 2},
        {"num": 9223372036854775807, "base": 2}
    ]
    for i, test_case in enumerate(test_cases, 1):
        num  = test_case['num']
        base = test_case['base']
        res = convert_from_decimal2(num, base)
        print(f"{i}. res:%064d <- num:{num}, base:{base}" % res)

if __name__ == '__main__':
    test()



