"""
Convert decimal to larger bases

[Expected Result]
-----------------
1. num:31, base:16, res:1F
2. num:10, base:16, res:A
3. num:15, base:16, res:F
4. num:16, base:16, res:10
5. num:81, base:16, res:51

"""

def convert_decimal_to_larger_bases(num, base):
    base_str = "0123456789ABCDEFGHIJKLMN"
    res = ""
    while num:
        res = base_str[num % base] + res
        num //= base
    return res

def test():
    test_cases = [
        {"num": 31, "base": 16},
        {"num": 10, "base": 16},
        {"num": 15, "base": 16},
        {"num": 16, "base": 16},
        {"num": 81, "base": 16}
   ] 
    for i, test_case in enumerate(test_cases, 1):
        num  = test_case['num']
        base = test_case['base']
        res  = convert_decimal_to_larger_bases(num, base)
        print(f"{i}. num:{num}, base:{base}, res:{res}")

if __name__ == '__main__':
    test()

