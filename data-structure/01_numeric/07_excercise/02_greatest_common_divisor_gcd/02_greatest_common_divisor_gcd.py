"""
Greatest Common Divisor (GCD)

1. gcd(2, 3) = 1
2. gcd(9, 6) = 3
3. gcd(12, 21) = 3
4. gcd(25, 7) = 1
5. gcd(24, 18) = 6

"""

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        res = b
        a, b = res, a % b
    return res

def test():
    test_cases = [
        {"a": 2, "b": 3},
        {"a": 9, "b": 6},
        {"a": 12, "b": 21},
        {"a": 25, "b": 7},
        {"a": 24, "b": 18}
    ]
    for i, test_case in enumerate(test_cases, 1):
        a, b = test_case['a'], test_case['b']
        res  = gcd(a, b)
        print(f"{i}. gcd({a}, {b}) = {res}")

if __name__ == '__main__':
    test()

        
