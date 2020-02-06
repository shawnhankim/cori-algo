"""
Generate num bit prime number

Expected Result:
3. res: 7
3. res: 5
3. res: 5
4. res: 11
4. res: 13
4. res: 13
4. res: 13

"""

import math
import random
import sys


def is_prime(num):
   if num < 2 or num == 4: return False
   if num <= 5: return True
   if not num%2 or not num%3 or not num%5: return False

   for i in range(6, int(math.sqrt(num))+1):
       if not num%i: return False
   return True


def generate_prime(num=3):
    while True:
        p = random.randint(pow(2, num-2), pow(2, num-1)-1)
        p = 2*p + 1
        if is_prime(p): return p


def main():
    if len(sys.argv) < 2:
        print("Usage: 02_generate_prime.py number")
        sys.exit()
    num = int(sys.argv[1])
    res = generate_prime(num)
    print(f"{num}. res: {res}")


if __name__ == '__main__':
    main()

