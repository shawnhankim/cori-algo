"""
Palindrome using Linked List

Expected Result: 

1. Is palindrome : True <- [1, 2, 3, 2, 1]
2. Is palindrome : True <- ['a', 'b', 'c', 'b', 'a']
3. Is palindrome : False <- [1, 2, 4, 4, 1]

"""

import copy

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head, self.tail = None, None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

class Palindrome(LinkedList):
    def is_palindrome(self, l1):
        if len(l1) < 2: return True
        if l1[0] != l1[-1]:  return False
        return self.is_palindrome(l1[1:-1])

    def is_linked_list_palindrome(self, l1):
        self.list_to_linked_list(l1)
        node = self.head
        l2 = []
        while node:
            l2.append(node.data)
            node = node.next
        return self.is_palindrome(l2)

    def list_to_linked_list(self, l1):
        for data in l1:
            self.add(data)


def test():
    test_cases = [
        [1, 2, 3, 2, 1],
        ['a', 'b', 'c', 'b', 'a'],
        [1, 2, 4, 4, 1]
    ]
    for i, l1 in enumerate(test_cases, 1):
        pl = Palindrome()
        res = pl.is_linked_list_palindrome(l1)
        print(f"{i}. Is palindrome : {res} <- {l1}")


if __name__ == '__main__':
    test()


