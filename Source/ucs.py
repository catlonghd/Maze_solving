from queue import PriorityQueue

class Base:
    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.start = start
        self.end = end
        self.wall_symbol = 'x'
        self.steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inside_matrix(self, point):
        if point[0] >= len(self.matrix) or point[0] < 0:
            return False
        if point[1] >= len(self.matrix[0]) or point[1] < 0:
            return False
        if self.matrix[point[0]][point[1]] == self.wall_symbol:
            return False
        return True

    def trace_path(self, trace):
        current = self.end
        path = []

        while current != self.start:
            path.append(current)
            current = trace[current]

        path.append(self.start)
        path.reverse()

        return path

def cost(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


class UCS(Base):
    def __int__(self, matrix, start, end):
        super().__init__(matrix, start, end)

    def find(self):
        visited, priority_queue = [], PriorityQueue()
        trace = {self.start: None}
        priority_queue.put([0, self.start])
        number_of_nodes = len(self.matrix) * len(self.matrix[0])
        distance = {}
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                distance[(i, j)] = float('inf')
        distance[self.start] = 0
        while not priority_queue.empty():
            dist, current = priority_queue.get()
            if current == self.end:
                break
            if dist > distance[current]:
                continue
            for step in self.steps:
                neighbor = (current[0] + step[0], current[1] + step[1])
                if self.inside_matrix(neighbor):
                    neighbor_cost = cost(neighbor, self.end)
                    neighbor_dist = distance[current] + neighbor_cost
                    if distance[neighbor] <= neighbor_dist:
                        continue
                    priority_queue.put([neighbor_dist, neighbor])
                    trace[neighbor] = current
                    distance[neighbor] = neighbor_dist

        return self.trace_path(trace)
