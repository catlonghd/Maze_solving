import matrixLib
import time
from collections import deque
import DFS_BFS
import math
from matrixLib import Manhattan,Euclid,Octile




def GBFS_search(matrix, start, end,heuristic): 
    begin = time.time()

    row = len(matrix)
    col = len(matrix[0])

    visited = [[False for i in range(col)]for j in range(row)]

    x = start[0]
    y = start[1]

    Dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    path = []
    # Mark the source cell as visited
    visited[x][y] = True
    greedy = {}
    # Create a queue for BFS
    q = deque()

    q.append(start) #  Enqueue source cell

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
                #calculate distance from point current to end
                dist = heuristic((a,b),end)
                store_dist[(a, b)] = dist
                greedy[(a,b)] = curr
            #select point based on distance array
            if i == 3:
                if store_dist == {}:
                    #if it doesn't quit traverse path to find a new way :v
                    for point in reversed(path):
                        for i in range(4):
                            a = point[0] + Dir[i][0]
                            b = point[1] + Dir[i][1]
                            if (a >= 0 and b >= 0 and a < row and b < col and matrix[a][b] != 'x' and (a, b) and not visited[a][b]):
                                dist = heuristic((a,b),end)
                                store_dist[(a, b)] = dist  
                                break
                store_dist = dict(sorted(store_dist.items(), key=lambda item: item[1]))
                for key, val in store_dist.items():
                    visited[key[0]][key[1]] = True
                    q.append(key)
                    break
    p = {}
    cell = end
    while cell != start:
        p[greedy[cell]] = cell 
        cell = greedy[cell]
    final = list(p.values())
    final.append(start)
    finalPath = final[::-1]
    close = time.time()

    return [len(greedy.keys()),finalPath,(close-begin)*1000]

def aStar_search(matrix, start, end,heuristic): 

    begin = time.time()

    row = len(matrix)
    col = len(matrix[0])
    
    visited = [[False for i in range(col)]for j in range(row)]

    x = start[0]
    y = start[1]

    Dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    path = []
    aStar = {}
    # Mark the source cell as visited
    visited[x][y] = True

    # Create a queue for BFS
    q = deque()
    
    q.append(start) #  Enqueue source cell
    store_dist = {}

    # Do a BFS starting from source cell
    while q:
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
                #calculate distance from point current to end
                dist_end = heuristic((a,b),end)
                dist_start = heuristic(start,(a,b))
                store_dist[(a, b)] = (dist_end + dist_start,dist_end, dist_start)
                aStar[(a,b)] = curr
            #select point based on distance array
            if i == 3:
                if store_dist == {}:
                    #if it doesn't quit traverse path to find a new way :v
                    for point in reversed(path):
                        for i in range(4):
                            a = point[0] + Dir[i][0]
                            b = point[1] + Dir[i][1]
                            if (a >= 0 and b >= 0 and a < row and b < col and matrix[a][b] != 'x' and (a, b) and not visited[a][b]):
                                dist_end = heuristic((a,b),end)
                                dist_start = heuristic(start,(a,b))
                                store_dist[(a, b)] = (dist_end + dist_start,dist_end, dist_start)
                                break
                store_dist = dict(sorted(store_dist.items(), key=lambda item: (item[1][0], item[1][1])))
                for key, val in store_dist.items():
                    visited[key[0]][key[1]] = True
                    q.append(key)
                    store_dist.pop(key)
                    break
    p = {}
    cell = end
    while cell != start:
        p[aStar[cell]] = cell 
        cell = aStar[cell]
    final = list(p.values())
    final.append(start)
    finalPath = final[::-1]
    
    close = time.time()

    return [len(aStar.keys()),finalPath,(close-begin)*1000]

def compareHeuristic_Greedy(matrix,bonus_points,start,end):
    len1_search = GBFS_search(matrix, start, end,Manhattan)[0]
    len2_search = GBFS_search(matrix, start, end,Euclid)[0]
    len3_search = GBFS_search(matrix, start, end,Octile)[0]

    len1_path = len(GBFS_search(matrix, start, end,Manhattan)[1])
    len2_path = len(GBFS_search(matrix, start, end,Euclid)[1])
    len3_path = len(GBFS_search(matrix, start, end,Octile)[1])

    time1 = GBFS_search(matrix, start, end,Manhattan)[2]
    time2 = GBFS_search(matrix, start, end,Euclid)[2]
    time3 = GBFS_search(matrix, start, end,Octile)[2]
    print(f'''\tSearch path Length of:
    Manhattan: {len1_search}
    Euclid: {len2_search}
    Octile: {len3_search}''')
    print(f'''\tFinal path Length of:
    Manhattan: {len1_path}
    Euclid: {len2_path}
    Octile: {len3_path}''')
    print(f'''\tRuntime(ms) of:
    Manhattan: {time1}
    Euclid: {time2}
    Octile: {time3}''')
    print('MANHATTAN:')
    plt1 = matrixLib.visualize_maze(matrix,bonus_points,start,end, GBFS_search(matrix, start, end,Manhattan)[1])
    print('EUCLID:')
    plt2 = matrixLib.visualize_maze(matrix,bonus_points,start,end, GBFS_search(matrix, start, end,Euclid)[1])
    print('OCTILE:')
    plt3 = matrixLib.visualize_maze(matrix,bonus_points,start,end, GBFS_search(matrix, start, end,Octile)[1])
    
    return [plt1, plt2, plt3]

def compareHeuristic_AStar(matrix,bonus_points,start,end):
    len1_search = aStar_search(matrix, start, end,Manhattan)[0]
    len2_search = aStar_search(matrix, start, end,Euclid)[0]
    len3_search = aStar_search(matrix, start, end,Octile)[0]

    len1_path = len(aStar_search(matrix, start, end,Manhattan)[1])
    len2_path = len(aStar_search(matrix, start, end,Euclid)[1])
    len3_path = len(aStar_search(matrix, start, end,Octile)[1])

    time1 = aStar_search(matrix, start, end,Manhattan)[2]
    time2 = aStar_search(matrix, start, end,Euclid)[2]
    time3 = aStar_search(matrix, start, end,Octile)[2]
    print(f'''\tSearch path Length of:
    Manhattan: {len1_search}
    Euclid: {len2_search}
    Octile: {len3_search}''')
    print(f'''\tFinal path Length of:
    Manhattan: {len1_path}
    Euclid: {len2_path}
    Octile: {len3_path}''')
    print(f'''\tRuntime(ms) of:
    Manhattan: {time1}
    Euclid: {time2}
    Octile: {time3}''')
    print('MANHATTAN:')
    plt1= matrixLib.visualize_maze(matrix,bonus_points,start,end, aStar_search(matrix, start, end,Manhattan)[1])
    print('EUCLID:')
    plt2 = matrixLib.visualize_maze(matrix,bonus_points,start,end, aStar_search(matrix, start, end,Euclid)[1])
    print('OCTILE:')
    plt3 = matrixLib.visualize_maze(matrix,bonus_points,start,end, aStar_search(matrix, start, end,Octile)[1])
    
    return [plt1, plt2, plt3]