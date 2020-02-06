

import math

max_h = 12
max_m = 60
bits  = max_m * [None]

def _add_res(res, h, m):
    res.append(f"{h}:{m:02d}")


def _num_bits(n):
    if not n: return 0
    bit = 0
    cnt = int(math.log(n, 2)) + 1
    for i in range(cnt):
        if n & 1 == 1: bit += 1
        n >>= 1
    return bit


def _init():
    for i in range(max_m):
        bits[i] = _num_bits(i)


def test_iterative_2d_array(n):
    res = []
    for h in range(max_h):
        for m in range(max_m):
            sum_bits = bits[h] + bits[m]
            if sum_bits == n: _add_res(res, h, m)
    return res


def test_backtracking_2d_array(n):
    res = []
    for h in range(max_h):
        helper(res, n, h)
    return res


def helper(res, n, h, m=0):
    if m == max_m: return
    sum_bits = bits[h] + bits[m]
    if sum_bits == n: _add_res(res, h, m)   
    helper(res, n, h, m+1)


def main():
    _init()
    for num in range(4):
        res1 = test_iterative_2d_array(num)
        res2 = test_backtracking_2d_array(num)
        print(f"\nRESULT-1: {res1}\nRESULT-2: {res2}")


if __name__ == '__main__':
    main()
