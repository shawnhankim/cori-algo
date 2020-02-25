"""

Validate balance parenthesis string using stack

Expected Results:

(((())))   -> True
[{()}]     -> True
[{()})     -> False

"""

def balance_parenthesis_str_with_stack(str1):
    stk = []
    par_set = {"(":")", "[":"]", "{":"}"}

    for c in str1:
        if c in par_set: stk.append(c)
        else:
            if c != par_set[stk.pop()]: return False
    res = False if len(stk) else True
    return res


def test():
    test_cases = [
        "(((())))",
        "[{()}]",
        "[{()})"
    ]
    for test_case in test_cases:
        res = balance_parenthesis_str_with_stack(test_case)
        print(f"{test_case:10} -> {res}")


if __name__ == '__main__':
    test()

