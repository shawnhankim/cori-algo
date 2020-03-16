"""
Merge Sort Files : O(n Log n)

Expected Results:

1. Test Case
   - File Name : 1.dat
     Data      : []
   - File Name : 2.dat
     Data      : []
   - File Name : 3.dat
     Data      : []
   - Merge Sort Files
     * []
     * []
     * []
   - Result of merge_sort_files() : []
   - Result of sorted()           : []
   - Assert merge_sort_files == sorted() : True

2. Test Case
   - File Name : 1.dat
     Data      : [1, 3, 5, 6, 8]
   - File Name : 2.dat
     Data      : [1, 3, 5, 7]
   - File Name : 3.dat
     Data      : [2, 3, 4, 5]
   - Merge Sort Files
     * [1, 3, 5, 6, 8]
     * [1, 1, 3, 3, 5, 5, 6, 7, 8]
     * [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
   - Result of merge_sort_files() : [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
   - Result of sorted()           : [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
   - Assert merge_sort_files == sorted() : True

3. Test Case
   - File Name : 1.dat
     Data      : [9, 1, 3, 5, 6, 8]
   - File Name : 2.dat
     Data      : [10, 1, 3, 5, 7]
   - File Name : 3.dat
     Data      : [2, 3, 11, 4, 5]
   - Merge Sort Files
     * [1, 3, 5, 6, 8, 9]
     * [1, 1, 3, 3, 5, 5, 6, 7, 8, 9, 10]
     * [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11]
   - Result of merge_sort_files() : [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11]
   - Result of sorted()           : [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11]
   - Assert merge_sort_files == sorted() : True

"""

def merge_sort_files(files):
    print("   - Merge Sort Files")
    res = []
    for fname in files:
        l1 = file_to_list(fname)
        l1 = merge_sort_list(l1) 
        res = merge_sort_two_lists(l1, res)
        print(f"     * {res}")
    return res


def merge_sort_two_lists(l1, l2):
    if not l1 or not l2: return l2 or l1

    res, i, j, len_l1, len_l2 = [], 0, 0, len(l1), len(l2)
    while i < len_l1 and j < len_l2:
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1

    if i >= len_l1 and j < len_l2: res.extend(l2[j:])
    if j >= len_l2 and i < len_l1: res.extend(l1[i:])
    return res


def merge_sort_list(l1):
    n = len(l1)
    if n < 2: return l1

    m = n >> 1
    l = merge_sort_list(l1[:m])
    r = merge_sort_list(l1[m:])

    res = []
    while l and r:
        if l[-1] >= r[-1]: res.append(l.pop())
        else             : res.append(r.pop())
    res.reverse()
    return (l or r) + res


def list_to_file(l1, fname):
    with open(fname, "w") as fp:
        for v in l1:
            fp.write(f"{v}\n")


def file_to_list(fname):
    res = []
    with open(fname, "r") as fp:
        for line in fp:
            res.append(int(line))
    return res


def test():
    test_cases = [
        [
            {"file": "1.dat", "data": []},
            {"file": "2.dat", "data": []},
            {"file": "3.dat", "data": []}
        ],
        [
            {"file": "1.dat", "data": [1, 3, 5, 6, 8]},
            {"file": "2.dat", "data": [1, 3, 5, 7]},
            {"file": "3.dat", "data": [2, 3, 4, 5]}
        ],
        [
            {"file": "1.dat", "data": [9, 1, 3, 5, 6, 8]},
            {"file": "2.dat", "data": [10, 1, 3, 5, 7]},
            {"file": "3.dat", "data": [2, 3, 11, 4, 5]}
        ]
    ]
    for i, test_case in enumerate(test_cases, 1):
        files, res2 = [], []
        print(f"\n{i}. Test Case")
        for t in test_case:
            file, data = t['file'], t['data']
            files.append(file)
            list_to_file(data, file)
            print(f"   - File Name : {file}")
            print(f"     Data      : {data}")
            res2.extend(data)
        res1 = merge_sort_files(files)
        res2 = sorted(res2)

        print(f"   - Result of merge_sort_files() : {res1}")
        print(f"   - Result of sorted()           : {res2}")
        print(f"   - Assert merge_sort_files == sorted() : {res1 == res2}")


if __name__ == '__main__':
    test()

        


