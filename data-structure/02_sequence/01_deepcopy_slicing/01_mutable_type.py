"""
Mutable Sequence Type with Deep Copy

Expected Result:

*** list deepcopy ***
l1: [1, 2, 3, 4]
l2: [1, 2, 3, 4]
l3: [1, 2, 3, 4]

*** set deepcopy ***
heroes: {'spyder'}
people: {'spyder', 'superman', 'ironman'}

*** set : object reference ***
heroes: {'spyder'}
people: {'spyder'}

*** dict : deepcopy***
dict1: {'name': 'test dictionary'}
dict2: {'name': 'test dictionary'}

*** other object : deepcopy***
obj1 (original obj): some other object
obj2 (shallow copy): some other object
obj3 (deep copy   ): some other object

"""

import copy

def list_deepcopy():
    l1 = [1, 2, 3, 4]
    l2 = l1[:]
    l3 = list(l2)

    print(f"*** list deepcopy ***")
    print(f"l1: {l1}")
    print(f"l2: {l2}")
    print(f"l3: {l3}")


def set_deepcopy():
    people = {"spyder", "superman", "ironman"}
    heroes = people.copy()
    heroes.discard("ironman")
    heroes.remove("superman")

    print(f"\n*** set deepcopy ***")
    print(f"heroes: {heroes}")
    print(f"people: {people}")

    h = people
    h.discard("ironman")
    h.remove("superman")

    print(f"\n*** set : object reference ***")
    print(f"heroes: {h}")
    print(f"people: {people}")


def dict_deepcopy():
    dict1 = {"name": "test dictionary"}
    dict2 = dict1.copy()

    print(f"\n*** dict : deepcopy***")
    print(f"dict1: {dict1}")
    print(f"dict2: {dict2}")


def other_object_deepcopy():
    obj1 = "some other object"
    obj2 = copy.copy(obj1)      # shallow copy
    obj3 = copy.deepcopy(obj2)  # deep copy

    print(f"\n*** other object : deepcopy***")
    print(f"obj1 (original obj): {obj1}")
    print(f"obj2 (shallow copy): {obj2}")
    print(f"obj3 (deep copy   ): {obj3}")


if __name__ == '__main__':
    list_deepcopy()
    set_deepcopy()
    dict_deepcopy()
    other_object_deepcopy()

