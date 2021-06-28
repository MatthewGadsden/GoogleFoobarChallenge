import heapq

class Node:

    def __init__(self, i, j, neighbours, wall) -> None:
        self.i = i
        self.j = j
        self.weight = float('inf')
        self.neighbours = neighbours
        self.wall = wall
        self.broken_wall = False
        self.finish = False
        self.on_heap = False
    
    def __gt__(self, other):
        if self.weight > other.weight:
            return True
        return False
    
    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        return False
    
    def __eq__(self, other):
        if self.weight == other.weight:
            return True
        return False

def create_nodes(map):
    h = len(map)
    w = len(map[0])
    start_node = None
    for row in range(h):
        for col in range(w):
            neighbours = []
            if row != 0:
                neighbours.append((row-1, col))
            if row != h-1:
                neighbours.append((row+1, col))
            if col != 0:
                neighbours.append((row, col-1))
            if col != w-1:
                neighbours.append((row, col+1))
            wall = map[row][col] == 1
            n = Node(row, col, neighbours, wall, )
            map[row][col] = n
            if row == 0 and col == 0:
                n.weight = 1
                start_node = n
            if row == h-1 and col == w-1:
                n.finish = True
    return start_node, map

def solution(map):
    current_node, map = create_nodes(map)
    heap = []
    while not current_node.finish:
        for (row, col) in current_node.neighbours:
            node = map[row][col]
            if current_node.broken_wall and node.wall:
                pass
            elif node.weight == current_node.weight + 1:
                if not current_node.broken_wall:
                    node.broken_wall = False
                if not node.on_heap:
                    node.on_heap = True
                    heap.append(node)
            elif current_node < node or (not node.on_heap and not current_node.broken_wall and node.broken_wall):
                node.weight = current_node.weight + 1
                if node.wall or current_node.broken_wall:
                    node.broken_wall = True
                else:
                    node.broken_wall = False
                if not node.on_heap:
                    node.on_heap = True
                    heap.append(node)

        heapq.heapify(heap)
        current_node = heapq.heappop(heap)
        current_node.on_heap = False
        if current_node.weight > 100:
            break
    return int(current_node.weight)

if __name__ == "__main__":
    ex_map2 =  [[0, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 0], 
                [0, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 1], 
                [0, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0]]
    
    ex_map1 =  [[0, 0, 0, 0], 
                [1, 1, 1, 0], 
                [0, 0, 0, 0], 
                [1, 1, 1, 1],
                [0, 0, 0, 0]]
    print(solution(ex_map1), end= "\n\n")
    print(solution(ex_map2))
