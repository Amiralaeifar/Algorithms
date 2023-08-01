from collections import deque  # --> for implementing a queue

#implementing graph in dictionary as an example
graph = {
    'you': ['mahkam','mahyar','sadra','arman'],
    'mahkam': ['mashahir', 'you'],
    'mahyar': ['zahra', 'sadra', 'you', 'sina'],
    'sadra': ['morva', 'mahyar', 'you'],
    'arman': ['you']
}

#imagine the wanted node is sina
def is_wanted(name):
    if name == 'sina':
        return True

#the actual algorithm
def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_wanted(person):
                return 'You found it'
            else:
                if graph.get(person):
                    search_queue += graph[person]
                    searched.append(person)
                else:
                    searched.append(person)
    return "didn't found"


print(breadth_first_search('you'))