"""
Animal Shelter using Deque

Expected Results:

1. Enqueue two cats and two dogs
- Cats : Bob Miya
- Dogs : Yoda Woof

2. Dequeue a dog and a cat
- Cats : Miya
- Dogs : Yoda Woof

3. Dequeue the old one
- Cats :
- Dogs : Yoda Woof

"""

class Node(object):
    def __init__(self, name=None, kind=None, next=None):
        self.name, self.kind, self.next, self.timestamp = name, kind, next, 0

class AnimalShelter(object):
    def __init__(self):
        self.head_cat = self.head_dog = self.tail_cat = self.tail_dog = None
        self.number = 0

    def enqueue(self, name, kind):
        self.number += 1
        new_animal = Node(name, kind)
        new_animal.timestamp = self.number

        if kind == "cat":
            if not self.head_cat: self.head_cat = new_animal
            if self.tail_cat: self.tail_cat.next = new_animal
            self.tail_cat = new_animal

        elif kind == "dog":
            if not self.head_dog: self.head_dog = new_animal
            if self.tail_dog: self.tail_dog.next = new_animal
            self.tail_dog = new_animal

    def dequeue_dog(self):
        if self.head_dog:
            animal = self.head_dog
            self.head_dog.next = animal.next
            return str(animal.name)
        else: print("Not found dog")

    def dequeue_cat(self):
        if self.head_cat:
            animal = self.head_cat
            self.head_cat = animal.next
            return str(animal.name)
        else: print("Not found cat")

    def dequeue_any(self):
        if self.head_cat and not self.head_dog:
            return self.dequeue_cat()
        elif self.head_dog and not self.head_cat:
            return self.dequeue_dog()
        elif self.head_cat and self.head_dog:
            if self.head_cat.timestamp < self.head_dog.timestamp:
                return self.dequeue_cat()
            else:
                return self.dequeue_dog()
        else:
            print("Not found animal")

    def print(self):
        print("- Cats :", end=" ")
        cat = self.head_cat
        while cat:
            print(cat.name, end=" ")
            cat = cat.next
        
        print("\n- Dogs :", end=" ")
        dog = self.head_dog
        while dog:
            print(dog.name, end=" ")
            dog = dog.next
        print()


def test():
    dq = AnimalShelter()
    print("\n1. Enqueue two cats and two dogs")
    dq.enqueue("Bob", "cat")
    dq.enqueue("Miya", "cat")
    dq.enqueue("Yoda", "dog")
    dq.enqueue("Woof", "dog")
    dq.print()

    print("\n2. Dequeue a dog and a cat")
    dq.dequeue_dog()
    dq.dequeue_cat()
    dq.print()

    print("\n3. Dequeue the old one")
    dq.dequeue_any()
    dq.print()


if __name__ == '__main__':
    test()


