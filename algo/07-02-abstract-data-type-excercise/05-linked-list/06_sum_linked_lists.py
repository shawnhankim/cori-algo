"""
Two Sum w/ Linked List

Expected Results:

1. Sum:   246 <- [1, 2, 3] + [1, 2, 3]
2. Sum: 46134 <- [4, 5, 6] + [4, 5, 6, 7, 8]

"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = self.tail = None

    def add(self, data):
        node = Node(data)
        if self.head is None: self.head = self.tail = node
        else: self.tail.next, self.tail = node, node

def list_to_linked_list(l1):
    ll = LinkedList()
    for data in l1:
        ll.add(data)
    return ll

def sum_linked_list(ll1, ll2):
    l1, l2 = [], []
    
    node = ll1.head
    while node:
        l1.append(node.data)
        node = node.next

    node = ll2.head
    while node:
        l2.append(node.data)
        node = node.next

    t, z = 0, 1
    while l1 and l2:
        a, b = l1.pop(), l2.pop()
        c = a + b
        d = c // 10
        e = c %  10
        t += e*z + 10*d*z
        z *= 10

    while l1:
        a = l1.pop()
        t += a*z
        z *= 10

    while l2:
        a = l2.pop()
        t += a*z
        z *= 10

    return t 

def test():
    test_cases = [
        {"l1": [1, 2, 3],    "l2": [1, 2, 3]},
        {"l1": [4, 5, 6],    "l2": [4, 5, 6, 7, 8]}
    ]
    for i, test_case in enumerate(test_cases, 1):
        l1, l2 = test_case['l1'], test_case['l2']
        ll1 = list_to_linked_list(l1)
        ll2 = list_to_linked_list(l2)
        res = sum_linked_list(ll1, ll2)
        print(f"{i}. Sum: {res:5} <- {l1} + {l2}")


if __name__ == '__main__':
    test()

