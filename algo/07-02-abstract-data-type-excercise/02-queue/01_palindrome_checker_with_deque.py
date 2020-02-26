"""
Palindrome using deque

Expected Results:

1. abcd dcba            -> Is palindrome : True
2. Madam Im Adam        -> Is palindrome : True
3. Buffy is a Slayer    -> Is palindrome : False

"""

from collections import deque

def is_palindrome(str1):
    dq = deque(str1.replace(" ", "").lower())
    while dq and len(dq) > 1:
        if dq.popleft() != dq.pop(): return False
    return True


def test():
    test_cases = [
        "abcd dcba",
        "Madam Im Adam",
        "Buffy is a Slayer"
    ]
    for i, test_case in enumerate(test_cases, 1):
        res = is_palindrome(test_case)
        print(f"{i}. {test_case:20} -> Is palindrome : {res}")


if __name__ == '__main__':
    test()

