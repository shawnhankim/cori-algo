"""
Circular Linked List

Expected Results:

- List : [ 0 1 2 3 4 ]
  * Is this a circular linked list : False
- List : [ 0 1 2 3 4 0 ]
  * Is this a circular linked list : True

"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.len  = 0

    def add(self, data=None, next=None):
        self.len += 1
        node = Node(data, next)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node


class CircularLinkedList(LinkedList):
    def _add(self, data):
        self.add(data, self.head)


def is_circular_linked_list(ll):
    s, f = ll.head, ll.head
    while s and f:
        try:
            s = s.next
            f = f.next.next
        except:
            return False
        if s == f: return True
    return False

def print_linked_list(ll):
    node = ll.head
    print("- List : [", end=" ")
    while node:
        print(f"{node.data}", end=" ")
        node = node.next
        if node == ll.head:
            print(f"{node.data} ]")
            return
    print("]")


def test():
    ll1 = LinkedList()
    for i in range(5):
        ll1.add(i)
    print_linked_list(ll1)
    res = is_circular_linked_list(ll1)
    print(f"  * Is this a circular linked list : {res}")

    ll2 = CircularLinkedList()
    for i in range(5):
        ll2._add(i)
    print_linked_list(ll2)
    res = is_circular_linked_list(ll2)
    print(f"  * Is this a circular linked list : {res}")


if __name__ == '__main__':
    test()


