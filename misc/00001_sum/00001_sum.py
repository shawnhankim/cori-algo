
def sum(arr):
    if not arr:
        return 0
    return arr[0] + sum(arr[1:])

test_cases = [
    [],
    [1],
    [1,2],
    [1,2,3]
]

for test_case in test_cases:
    print(f"{test_case} : {sum(test_case)}")

