from DFS_BFS import bfs_search
from matrixLib import Euclid
from Greedy_AStar import aStar_search
from collections import deque



def Astar_bonus(matrix, start, end,bonus_points):
    row = len(matrix)
    col = len(matrix[0])
    weights = [[1 for i in range(col)]for j in range(row)]
    for k in bonus_points:
        weights[k[0]][k[1]] = k[2]

    visited = [[False for i in range(col)]for j in range(row)]
    x = start[0]
    y = start[1]


    Dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    bfs = {}
    bfs_length = {}
    path = []
    # Mark the source cell as visited
    visited[x][y] = True

    # Create a queue for BFS
    q = deque()

    q.append(start) #  Enqueue source cell
    #store_dist = {}
    # Do a BFS starting from source cell
    while q:

        store_dist = {}
        curr = q.popleft() # Dequeue the front cell
        path.append(curr)
        # If we have reached the destination cell,
        # we are done
        if curr[0] == end[0] and curr[1] == end[1]:
            break
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            a = curr[0] + Dir[i][0]
            b = curr[1] + Dir[i][1]    

        # if adjacent cell is valid, has path 
        # and not visited yet, enqueue it.
            if (a >= 0 and b >= 0 and a < row and b < col and matrix[a][b] != 'x' and (a, b) and not visited[a][b]):
                dist = Euclid((a,b),end)
                store_dist[(a, b)] = weights[a][b] + dist
                bfs[(a, b)] = curr
                #select point based on distance array
            if i == 3:
                if store_dist == {}:
                    q.append(bfs[curr])
                    continue
                store_dist = dict(sorted(store_dist.items(), key=lambda item: item[1]))
                min_dist = [val for key,val in store_dist.items() if store_dist[key] == min(store_dist.values())]
                if len(min_dist) > 1 and len(set(min_dist)) == 1:
                    for key, val in store_dist.items():
                        bfs_length[key] = len(bfs_search(matrix,key,end))
                    bfs_length = dict(sorted(bfs_length.items(), key=lambda item: item[1]))
                    for k,length in bfs_length.items():
                        visited[k[0]][k[1]] = True
                        q.append(k)
                        #store_dist.pop(k)
                        break
                else:
                    for key, val in store_dist.items():
                        visited[key[0]][key[1]] = True
                        q.append(key)
                        #store_dist.pop(key)
                        break
    p = {}
    cell = end
    while cell != start:
        p[bfs[cell]] = cell 
        cell = bfs[cell]
        for key,val in bfs.items():
            if val == cell and key not in p.keys() and weights[key[0]][key[1]] < 0:
                p[key] = cell
                p[str(key)+'-sub'] = key
                break
    final = list(p.values())
    final.append(start)
    finalPath = final[::-1]
    return finalPath

#calculate and shorted distance from start to all bonus point
def sort_bonus_point(start,bonus_points):
    store_dist_from_start = {}
    for point in bonus_points:
        store_dist_from_start[point[:2]] = Euclid(start, point[:2])

    store_dist_from_start = dict(sorted(store_dist_from_start.items(), key=lambda item: item[1]))
    return store_dist_from_start

def cost_func(matrix,dist,bonus_points):
    row = len(matrix)
    col = len(matrix[0])
    weights = [[1 for i in range(col)]for j in range(row)]
    for k in bonus_points:
        weights[k[0]][k[1]] = k[2]
    finalPath = dist
    cost = 0
    for x in finalPath[1:]:
        cost += weights[x[0]][x[1]]
        weights[x[0]][x[1]] = 1
    return cost

def all_real_cost(matrix,start,end,bonus_points):
    store_dist_from_start = sort_bonus_point(start,bonus_points)
    #calculate all real cost from A to B point
    
    #first from start point
    start_dist = {}
    for point in store_dist_from_start.keys():
        dist_from_start = aStar_search(matrix, start, point, Euclid)
        start_dist[(start, point)] = cost_func(matrix,dist_from_start[1],bonus_points)

    #second point to point
    points_dist = {}
    for i, point_i in enumerate(list(store_dist_from_start.keys())):
        for j, point_j in enumerate(list(store_dist_from_start.keys())):
            if i != j:
                dist_from_point = aStar_search(matrix, point_i, point_j, Euclid)
                points_dist[(point_i, point_j)] = cost_func(matrix,dist_from_point[1],bonus_points)

    #third point to end
    end_dist = {}
    for point in store_dist_from_start.keys():
        dist_from_start = aStar_search(matrix, point, end, Euclid)
        end_dist[(point, end)] = cost_func(matrix,dist_from_start[1],bonus_points)

    #last start to end
    dist_from_start = aStar_search(matrix, start, end, Euclid)
    start_end_dist = {}
    start_end_dist[(start, end)] = cost_func(matrix,dist_from_start[1],bonus_points)

    points_dist.update(start_dist)
    points_dist.update(end_dist)
    return [points_dist, start_end_dist]


def sort_distance(matrix,start,end,bonus_points):
    # sorted distance
    points_dist = all_real_cost(matrix,start,end,bonus_points)[0]
    points_dist = dict(sorted(points_dist.items(), key=lambda item: item[1]))
    return points_dist

def triangle_distance(matrix,start,end,bonus_points):
    # using triangle distance
    G_cost = 0 #cost from start to point
    H_cost = 0 #cost from point to end
    start_end_cost =  list(all_real_cost(matrix,start,end,bonus_points)[1].values())[0]  #cost from start to end
    
    points_dist = sort_distance(matrix,start,end,bonus_points)
    start_point = start
    # first point
    store_point_path = []
    for point in bonus_points:
        G_cost = points_dist[(start_point, point[:2])]
        H_cost = points_dist[(point[:2], end)]

        if G_cost + H_cost < start_end_cost:
            store_point_path.append(point[:2])
            start_point = point[:2]
            start_end_cost = H_cost 
    return store_point_path


def bonus_search_2(matrix,bonus_points,start,end):
    #try to go store_point_path
    first = start
    second = end
    path = []
    store_point_path = triangle_distance(matrix,start,end,bonus_points)
    
    row = len(matrix)
    col = len(matrix[0])
    weights = [[1 for i in range(col)]for j in range(row)]
    for k in bonus_points:
        weights[k[0]][k[1]] = k[2]

    for point in store_point_path:
        second = point
        path += Astar_bonus(matrix, first, second,bonus_points)
        #recover weights
        for bonus in bonus_points:
            if bonus[:2] in path:
                weights[bonus[:2][0]][bonus[:2][1]] = 1
        first = point

    second = end
    path += Astar_bonus(matrix, first, second, bonus_points)
    return path
    