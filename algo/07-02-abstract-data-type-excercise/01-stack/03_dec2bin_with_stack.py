"""
Decimal to binary using stack

Expected Results:

Decimal 9 -> Binary 1001
Decimal 8 -> Binary 1000
Decimal 2 -> Binary 10
Decimal 0 -> Binary 0

"""

def dec2bin_with_stack(decnum):
    if not decnum: return '0'
    stk, str_list, res = [], [], ''
    while decnum:
        b = decnum % 2
        decnum //= 2
        stk.append(b)
    while stk:
        str_list.append(str(stk.pop()))
    return ''.join(str_list)


def test():
    test_cases = [9, 8, 2, 0]
    for decnum in test_cases:
        res = dec2bin_with_stack(decnum)
        print(f"Decimal {decnum} -> Binary {res}")


if __name__ == '__main__':
    test()

