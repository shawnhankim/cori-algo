
def reverse_string_with_stack(str1):
    stk, lists = [], []

    for c in str1:
        stk.append(c)

    while stk:
        lists.append(stk.pop())

    res = ''.join(lists)
    return res


if __name__ == '__main__':
    test_str = 'I am an angel.'
    res = reverse_string_with_stack(test_str)
    print(res)


