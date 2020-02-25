"""
Hash Table

Expected Result:

Slot 0
[ 0 3 6 9 12 15 18 ]
Slot 1
[ 1 4 7 10 13 16 19 ]
Slot 2
[ 2 5 8 11 14 17 ]
Deleting item 0, 1, 2...
Slot 0
[ 3 6 9 12 15 18 ]
Slot 1
[ 4 7 10 13 16 19 ]
Slot 2
[ 5 8 11 14 17 ]

"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data, self.next = data, next
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data
 
    def set_next(self, next):
        self.next = next

class LinkedListFIFO(object):
    def __init__(self):
        self.head, self.len, self.tail = None, 0, None

    def print_list(self):
        node = self.head
        print("[", end=" ")
        while node:
            print(node.data, end=" ")
            node = node.next
        print("]")

    def add_first(self, data):
        self.len, node = 1, Node(data)
        self.head = self.tail = node

    def del_first(self):
        self.len, self.head, self.tail = 0, None, None
        print("Linked list is empty.")

    def add(self, data):
        self.len += 1
        node = Node(data)
        if self.tail: self.tail.next = node
        self.tail = node

    def add_node(self, data):
        if not self.head: self.add_first(data)
        else            : self.add(data)

    def find(self, idx):
        prev, node, i = None, self.head, 0
        while node and i < idx:
            prev, node, i = node, node.next, i+1
        return node, prev, i

    def find_by_data(self, data):
        prev, node, found = None, self.head, False
        while node and not found:
            if node.data == data: found = True
            else: prev, node = node, node.next
        return node, prev, found

    def del_node(self, idx):
        if not self.head or not self.head.next: self.del_first()
        else:
            node, prev, i = self.find(idx)
            if i == idx and node:
                self.len -= 1
                if i == 0 or not prev: self.head = self.tail = node.next
                else:                  prev.next = node.next
            else:
                print(f"Not found node[{i}]")
    
    def del_node_by_data(self, data):
        if not self.head or not self.head.next:
            self.del_first()
        else: 
            node, prev, i = self.find_by_data(data)
            if node and node.data == data:
                self.len -= 1
                if i == 0 or not prev: self.head = self.tail = node.next
                else: prev.next = node.next
            else: 
                print(f"Not found node's data with {data}")

class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._create_hash_table()

    def _create_hash_table(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())
    
    def _find(self, data):
        return data % self.size

    def add(self, data):
        idx = self._find(data)
        self.slots[idx].add_node(data)

    def delete(self, data):
        idx = self._find(data)
        self.slots[idx].del_node_by_data(data)

    def print(self):
        for i in range(self.size):
            print(f"Slot {i}")
            self.slots[i].print_list()
               
      
def test_hash_table():
    hs = HashTableLL(3)
    for i in range(20):
        hs.add(i)
    hs.print()
    print("Deleting item 0, 1, 2...")
    for i in range(3):
        hs.delete(i)
    hs.print()


if __name__ == '__main__':
    test_hash_table()

