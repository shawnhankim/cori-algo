
import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._idx  = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._idx, item))
        self._idx += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({0!r})".format(self.name)        


def test_priority_queue():
    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test2'), 4)
    q.push(Item('test3'), 3)
    assert(str(q.pop()) == "Item('test2')")
    print("Passed test")


if __name__ == '__main__':
    test_priority_queue()

