from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller.")
                return True
            search_queue += graph[person]
            searched.append(person)
    return False

test_cases = ["you", "peggy", "thom", "jonny"]
for test_case in test_cases:
    if not search(test_case):
        print(f"Unable to find a mango seller from this person({test_case}).")
