
"""
Covert to decimal

2 <= base <= 10

[Expected Result]
-----------------
1. res:   9 <- num:0000000000000000000000000000000000000000000000000000000000001001, base:2
2. res:   1 <- num:0000000000000000000000000000000000000000000000000000000000000001, base:2
3. res:   2 <- num:0000000000000000000000000000000000000000000000000000000000000010, base:2
4. res:  17 <- num:0000000000000000000000000000000000000000000000000000000000010001, base:2
5. res:  35 <- num:0000000000000000000000000000000000000000000000000000000000100011, base:2

"""

def convert_to_decimal(num, base):
    res = 0
    i = 0
    while num:
        denominator = num % 10
        if denominator == 1:
            res += base**i            
        i += 1
        num //= 10
    return res    

def convert_to_decimal1(num, base):
    multiplier, res = 1, 0
    while num > 0:
        res += num % 10 * multiplier
        multiplier *= base
        num //=10
    return res

def test():
    test_cases = [
        {"num": 1001  , "base": 2},
        {"num": 1     , "base": 2},
        {"num": 10    , "base": 2},
        {"num": 10001 , "base": 2},
        {"num": 100011, "base": 2}
    ]
    for i, test_case in enumerate(test_cases, 1):
        num  = test_case['num']
        base = test_case['base']
        res  = convert_to_decimal1(num, base)
        print(f"{i}. res:%4d <- num:%064d, base:{base}" % (res, num))

if __name__ == '__main__':
    test()

