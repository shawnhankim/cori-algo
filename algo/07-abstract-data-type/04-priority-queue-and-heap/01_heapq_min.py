
import heapq

#
# [4, 6, 8, 1]
# [1, 4, 8, 6]
#
list1 = [4, 6, 8, 1]
print(list1)
heapq.heapify(list1)
print(list1)


#
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
#
h = []
heapq.heappush(h, (1, 'a'))
heapq.heappush(h, (2, 'b'))
heapq.heappush(h, (3, 'c'))
heapq.heappush(h, (4, 'd'))
print(h)


"""
[4, 6, 8, 1]
[1, 4, 8, 6]
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
list : [1, 4, 8, 6]
pop  : 1
list : [4, 6, 8]
pop  : 4
list : [6, 8]
pop  : 6
list : [8]
pop  : 8
list : []
"""
list2 = list1
print(f"list : {list2}")
while list2:
    a = heapq.heappop(list2)
    print(f"pop  : {a}")
    print(f"list : {list2}")


#
# merged heap : [ 1 2 3 4 5 6 ]
#
m = heapq.merge([1,3,5], [2,4,6])
print("merged heap : [", end=" ")
for x in m:
    print(f"{x}", end=" ")
print("]")

