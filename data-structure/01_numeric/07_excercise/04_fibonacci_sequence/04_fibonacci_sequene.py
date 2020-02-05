"""
Fibonacci

Expected Output:

f(0) = [0, 0, 0]
f(1) = [1, 1, 1]
f(2) = [2, 2, 1]
f(3) = [3, 3, 3]
f(5) = [8, 8, 8]
f(10) = [89, 89, 88]
f(11) = [144, 144, 144]
f(12) = [233, 233, 232]
f(55) = [225851433717, 225851433717, 225851433717]
f(70) = [308061521170129, 308061521170129, 308061521170129]
"""

import math

def fibo(n):
    if n < 2: return n
    f = [1, 1]
    for i in range(2, n+1):
        fn = f[i-1] + f[i-2]
        f.append(fn)
    return f[n]


def fibo2(n):
    if n < 2: return n
    a, b = 0, 1
    for i in range(n+1):
        a, b = b, a+b
    return a


def fibo3(n):
    if n < 2: return n
    return fibo3(n-1) + fibo3(n-2)


def fibo5(n):
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** (n+1) / sq5))


def main():
    test_cases = [0, 1, 2, 3, 5, 10, 11, 12, 55, 70]
    for test_case in test_cases:
        n = test_case
        f = [fibo(n), fibo2(n), fibo5(n)]
        print(f"f({test_case}) = {f}")


if __name__ == '__main__':
    main()

