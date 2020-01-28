

# False
res = 0.2 * 3 == 0.6
print(res)

# True
res = 1.2 - 0.2 == 1.0
print(res)

# False
res = 1.2 - 0.1 == 1.1
print(res)

# False
res = 0.1 * 0.1 == 0.01
print(res)

def a(x, y, places=7):
    return round(abs(x-y), places) == 0

# False
res = a(1.2, 0.1)
print(res)
