import matrixLib
from DFS_BFS import bfs_search
def bonus_search_1(matrix,bonus_points,start, end): 
    
    bonus_dict = {}
    path_dict = {}
    for bonus in bonus_points:
        bonus_dict[(bonus[0], bonus[1])] = bonus[2]
    bonus_dict = dict(sorted(bonus_dict.items(),key=lambda item: (item[1])))

        
    row = len(matrix)
    col = len(matrix[0])
    weights = [[1 for i in range(col)]for j in range(row)]
    for k in bonus_points:
        weights[k[0]][k[1]] = k[2]

    for x in bonus_dict.keys():
        len_path = len(bfs_search(matrix,start,x))
        path_dict[x] = len_path + weights[x[0]][x[1]]
    visited = [[False for i in range(col)]for j in range(row)]
 
    x = start[0]
    y = start[1]


    Dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    path = []
    # Mark the source cell as visited
    visited[x][y] = True

    curr = start
    while True:
        store_dist = {}
        bfs_length = {}
        path.append(curr)
        # If we have reached the destination cell,we are done
        if curr[0] == end[0] and curr[1] == end[1]:
            break
        for i in range(4):
            a = curr[0] + Dir[i][0]
            b = curr[1] + Dir[i][1]    
        # if adjacent cell is valid, has path and not visited yet, get f(n)
            if (a >= 0 and b >= 0 and a < row and b < col and matrix[a][b] != 'x' and (a, b) and not visited[a][b]):
                for x in bonus_dict.keys():
                    len_path = len(bfs_search(matrix,(a,b),x))
                    dist =  len_path + weights[x[0]][x[1]]
                    path_dict[x] = dist
                path_dict = dict(sorted(path_dict.items(),key=lambda item: (item[1])))
                for key,val in path_dict.items():
                    dist = val
                    break
                if dist > matrixLib.Euclid((a,b),end):
                    dist = matrixLib.Euclid((a,b),end)
                store_dist[(a, b)] = dist
            if i == 3:
                if store_dist == {}:
                    path.remove(curr)
                    if path[-1] == curr:
                         path.remove(curr)
                    curr = path[-1]
                    break
                    
                store_dist = dict(sorted(store_dist.items(), key=lambda item: item[1]))
                min_dist = [val for key,val in store_dist.items() if store_dist[key] == min(store_dist.values())]
                if len(min_dist) > 1 and len(set(min_dist)) == 1:
                    for key, val in store_dist.items():
                        bfs_length[key] = len(bfs_search(matrix,key,end)) 
                    bfs_length = dict(sorted(bfs_length.items(), key=lambda item: item[1]))
                    for k,length in bfs_length.items():
                        visited[k[0]][k[1]] = True
                        curr = k
                        if k in bonus_dict.keys():
                            bonus_dict.pop(k)
                            path_dict.pop(k)
                            visited = [[False for i in range(col)]for j in range(row)]
                        break
                else:
                    for key, val in store_dist.items():
                        visited[key[0]][key[1]] = True
                        curr = key
                        if key in bonus_dict.keys():
                            bonus_dict.pop(key)
                            path_dict.pop(key)
                            visited = [[False for i in range(col)]for j in range(row)]
                        break
    cost = 0
    for x in path[1:]:
         cost += weights[x[0]][x[1]]
    return [cost,path]