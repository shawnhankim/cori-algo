"""
Check if it is the prime number

Expected Result:

Is prime( 0) : res1(0), res2(0)
Is prime( 1) : res1(0), res2(0)
Is prime( 2) : res1(1), res2(1)
Is prime( 3) : res1(1), res2(1)
Is prime( 4) : res1(0), res2(0)
Is prime( 5) : res1(1), res2(1)
Is prime( 6) : res1(0), res2(0)
Is prime( 7) : res1(1), res2(1)
Is prime( 8) : res1(0), res2(0)
Is prime( 9) : res1(0), res2(0)
Is prime(10) : res1(0), res2(0)
Is prime(11) : res1(1), res2(1)
Is prime(12) : res1(0), res2(0)
Is prime(13) : res1(1), res2(1)
Is prime(14) : res1(0), res2(0)
Is prime(15) : res1(0), res2(0)
Is prime(16) : res1(0), res2(0)
Is prime(17) : res1(1), res2(1)
Is prime(18) : res1(0), res2(0)
Is prime(19) : res1(1), res2(1)

"""

import math

def is_prime1(num):
    if num < 2: return False
    if num == 2 or num == 3 or num == 5: return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0: return False

    for i in range(6, num):
        if num % i == 0: return False
    return True


def is_prime2(num):
    if num < 2 or num == 4: return False
    if num <= 5: return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0: return False

    for i in range(6, int(math.sqrt(num))+1):
        if num % i == 0: return False
    return True


def test():
    max_test_cnt = 20
    for num in range(max_test_cnt):
        res1 = is_prime1(num)
        res2 = is_prime2(num)
        print(f"Is prime({num:2}) : res1({res1:1}), res2({res2:1})")
 

if __name__ == '__main__':
    test()

