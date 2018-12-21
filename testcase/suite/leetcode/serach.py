from collections import deque

def search(name):
    search_deque = deque()
    search_deque += graph[name]

    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("Bingo")
                return True
            else:
                search_deque += graph[person]
                searched.append(person)
    return False
