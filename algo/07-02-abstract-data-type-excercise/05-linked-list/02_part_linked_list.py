"""
Partiition linked list 

Expected result:

1. list:[6, 7, 3, 4, 9, 5, 1, 2, 8], n:6 -> result:[3, 4, 5, 1, 2, 6, 7, 9, 8]
2. list:[8, 9, 1, 2, 3, 6, 7, 4, 5], n:4 -> result:[1, 2, 3, 4, 8, 9, 6, 7, 5]

"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = self.tail = None 

    def add(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node

class PartitionLinkedList(LinkedList):
    def list_to_linked_list(self, l1):
        for data in l1:
            self.add(data)

    def partition_list(self, n):
        l, r = LinkedList(), LinkedList()

        node = self.head
        while node:
            if   node.data < n: l.add(node.data)
            elif node.data > n: r.add(node.data)
            node = node.next
        l.add(n)

        node = r.head
        while node:
            l.add(node.data)
            node = node.next

        l1 = []
        node = l.head
        while node:
            l1.append(node.data)
            node = node.next
        return l1

def test():
    test_cases = [
        {"list": [6, 7, 3, 4, 9, 5, 1, 2, 8], "n": 6},
        {"list": [8, 9, 1, 2, 3, 6, 7, 4, 5], "n": 4}
    ]
    for i, test_case in enumerate(test_cases, 1):
        l1, n = test_case['list'], test_case['n']
        ll = PartitionLinkedList()
        ll.list_to_linked_list(l1)
        res = ll.partition_list(n)
        print(f"{i}. list:{l1}, n:{n} -> result:{res}")


if __name__ == '__main__':
    test()

    
