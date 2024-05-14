import random
import math

# batangas_map = {
#     1 : (13.638008, 121.146661),
#     2 : (13.637916, 121.083202),
#     3 : (13.670183, 121.119514),
#     4 : (13.722023, 121.132917),
#     5 : (13.716311, 121.158934),
#     6 : (13.755276, 121.059078),
#     7 : (13.710711, 121.171138),
#     8 : (13.767370, 121.063439),
#     9 : (13.755979, 121.068831),
#     10 : (13.765389, 121.113450)
# }

batangas_map = {
    1 : (13.638008, 121.146661),
    2 : (13.637916, 121.083202),
    3 : (13.670183, 121.119514),
    4 : (13.722023, 121.132917),
    5 : (13.716311, 121.158934),
    6 : (13.755276, 121.059078),
    7 : (13.710711, 121.171138),
    8 : (13.767370, 121.063439),
    9 : (13.755979, 121.068831),
    10 : (13.765389, 121.113450)
}


parents = []


def generate_rand():
    parent = []
    while len(parent) <= 9:
        temp_gene = random.sample(list(set(range(1, 11)) - set(parent)), 1)[0]
        parent.append(temp_gene)
    if parent not in parents:
        parents.append(parent)
        print(parent)
        return parent
    else:
        generate_rand()

def distance(parent):
    total_distance = 0
    for i, gene in enumerate(parent):
        curr_lat, curr_lon = batangas_map[gene]

        if i < len(parent) - 1:
            next_gene = parent[i + 1]
            next_lat, next_lon = batangas_map[next_gene]
            temp_distance =  math.sqrt((next_lon - curr_lon)**2 + (next_lat - curr_lat)**2)
            total_distance += temp_distance

    print(f"Total distance: {total_distance}")

parent = generate_rand()

distance(parent)

































class List:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)

    def insert(self, index, item):
        self.items.insert(index, item)

    def pop(self, index=-1):
        return self.items.pop(index)

    def index(self, item):
        return self.items.index(item)

    def count(self, item):
        return self.items.count(item)

    def reverse(self):
        self.items.reverse()

    def clear(self):
        self.items.clear()