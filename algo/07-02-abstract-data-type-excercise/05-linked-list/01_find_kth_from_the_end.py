"""
Find kth data from last index of linked list

Expected result:

1. result: 4 <- k: 2 from list[1, 2, 3, 4, 5]
2. result: 8 <- k: 3 from list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node


class KthFromLast(LinkedList):
    def find_kth_to_last(self, k):
        p1 = p2 = self.head
        i, j = 0, k-1
        while p1:
            if i > j:
                try:
                    p2 = p2.next
                except:
                    break
            p1 = p1.next
            i += 1
        return p2.data


def test():
    test_cases = [
        {"list": [1, 2, 3, 4, 5]                , "k": 2},
        {"list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "k": 3}
    ]
    for i, test_case in enumerate(test_cases, 1):
        l1, k = test_case['list'], test_case['k']
        ll = KthFromLast()
        for data in l1:
            ll.add(data)
        res = ll.find_kth_to_last(k)
        print(f"{i}. result: {res} <- k: {k} from list{l1}")


if __name__ == '__main__':
    test()

