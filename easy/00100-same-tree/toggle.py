"""
0. toggle = 1
1. toggle = 0
2. toggle = 1
3. toggle = 0
4. toggle = 1
5. toggle = 0
6. toggle = 1
7. toggle = 0
8. toggle = 1
9. toggle = 0
"""

toggle = 0

for i in range(10):
    toggle ^= 1
    print(f"{i}. toggle = {toggle}")
