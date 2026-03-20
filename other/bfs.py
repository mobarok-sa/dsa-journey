
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['peggy'] = []
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []


# helper function
def person_is_seller(name):
    return name[-1] == 'm'

from collections import deque 

def search(name):
    src_queue = deque()
    src_queue += graph[name]
    searched = []
    while src_queue:
        person = src_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person, "is a mango seller!")
                return True 
            else:
                src_queue += graph[person]
                searched.append(person)
    return False

search('you')

