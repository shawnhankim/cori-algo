"""
Mutable Sequence Type with Deep Copy

Expected Result:

*** list deepcopy ***
l1: [1, 2, 3, 4]
l2: [1, 2, 3, 4]
l3: [1, 2, 3, 4]

*** set deepcopy ***
heroes: {'spyder'}
people: {'superman', 'spyder', 'ironman'}

*** set : object reference ***
heroes: {'spyder'}
people: {'spyder'}

"""


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


if __name__ == '__main__':
    list_deepcopy()
    set_deepcopy()

