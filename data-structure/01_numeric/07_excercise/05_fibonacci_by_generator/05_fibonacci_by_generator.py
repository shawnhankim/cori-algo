"""
Fibonacci Sequence Generator

Expected Result:
1 1 2 3 5 8 13 21 34 55

"""


def fib_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

def main():
    fb = fib_generator()
    for _  in range(10):
        print(next(fb), end= " ")
    print()

if __name__ == '__main__':
    main()

