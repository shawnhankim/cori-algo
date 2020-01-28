
res = sum(0.1 for i in range(10)) == 1.0
print(res)

from decimal import Decimal
res = sum(Decimal("0.1") for i in range(10)) == Decimal("1.0")
print(res)

