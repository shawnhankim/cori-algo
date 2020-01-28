
test_cases = [0, 1, 2, 3, 4, 8, 9, 99, 999]
for num in test_cases:
    print(f"\n[%03d] binary : {bin(num)}" % (num))
    print(f"[%03d] octal  : {oct(num)}" % (num))
    print(f"[%03d] hexa   : {hex(num)}" % (num))

""" Result:

[000] binary : 0b0
[000] octal  : 0o0
[000] hexa   : 0x0

[001] binary : 0b1
[001] octal  : 0o1
[001] hexa   : 0x1

[002] binary : 0b10
[002] octal  : 0o2
[002] hexa   : 0x2

[003] binary : 0b11
[003] octal  : 0o3
[003] hexa   : 0x3

[004] binary : 0b100
[004] octal  : 0o4
[004] hexa   : 0x4

[008] binary : 0b1000
[008] octal  : 0o10
[008] hexa   : 0x8

[009] binary : 0b1001
[009] octal  : 0o11
[009] hexa   : 0x9

[099] binary : 0b1100011
[099] octal  : 0o143
[099] hexa   : 0x63

[999] binary : 0b1111100111
[999] octal  : 0o1747
[999] hexa   : 0x3e7

"""
