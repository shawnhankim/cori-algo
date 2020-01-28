
test_cases = [0, 1, 2, 3, 4, 8, 9, 99, 999]
for num in test_cases:
    print(f"\n[%03d] binary : {bin(num)}" % (num))
    print(f"[%03d] octal  : {oct(num)}" % (num))
    print(f"[%03d] hexa   : {hex(num)}" % (num))

