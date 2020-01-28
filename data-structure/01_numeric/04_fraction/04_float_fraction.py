from fractions import Fraction

def rounding_floats(number, places):
    return round(number, places)

def float_to_fractions(num):
    return Fraction(*num.as_integer_ratio())

def get_denominator(num1, num2):
    a = Fraction(num1, num2)
    return a.denominator

def get_numerator(num1, num2):
    a = Fraction(num1, num2)
    return a.numerator

def test_floats():
    num1 = 1.25
    num2 = 1
    num3 = -1
    num4 = 5/4
    num5 = 6
    assert(rounding_floats   (num1   , num2) == 1.2)
    assert(rounding_floats   (num1*10, num3) == 10)
    assert(float_to_fractions(num1)          == num4)
    assert(get_denominator   (num2   , num5) == num5)
    assert(get_numerator     (num2   , num5) == num2)
    print("Test has been passed!")

if __name__ == "__main__":
    test_floats()


