
strings = [ "[1,2,3]", "[[1,2,3]]" ]

for s in strings:
    tmp1 = s.strip()
    tmp2 = tmp1[1:-1]
    tmp3 = tmp1[2:-2]
    tmp4 = tmp1[-1]
    tmp5 = tmp1[-1:]
    tmp6 = tmp1[-1:1]
    print(f"{s} : [1] {tmp1}, [2] {tmp2}, [3] {tmp3}, [4] {tmp4}, [5] {tmp5}, [6] {tmp6}")


