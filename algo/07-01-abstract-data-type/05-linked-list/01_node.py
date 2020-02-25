
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

"""
Expected Results:
c
a
b
aa
e
"""
if __name__ == '__main__':
    l = Node("a", Node("b", Node("c", Node("d"))))
    nn_data = l.next.next.data
    print(f"{nn_data}")
    assert(nn_data == "c")

    print(l.get_data())
    print(l.get_next().get_data())
    l.set_data("aa")
    l.set_next(Node("e"))
    print(l.get_data())
    print(l.get_next().get_data())


