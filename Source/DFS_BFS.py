from collections import deque
def dfs_search(matrix, start, end):    
    row = len(matrix)
    col = len(matrix[0])

    x = start[0]
    y = start[1]

    Dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    path = []
    stack = []
    stack.append((x,y))
    dfs = {}
    while end not in stack:

        s = stack[-1]
        if s not in path:
            path.append(s)
        #print(f'Curr: {s}')
        for i in range(4) :
            # using the direction array
            a = s[0] + Dir[i][0]
            b = s[1] + Dir[i][1]

            # not blocked and valid
            if(a >= 0 and b >= 0 and a < row and b < col and matrix[a][b] != 'x' and (a, b) not in path):
                stack.append((a, b))
                dfs[(a,b)] = s
                break
            if(i == 3 ):
                for j in range(4):
                    a1 = s[0] + Dir[j][0] 
                    b1 = s[1] + Dir[j][1]
                    if (a1,b1) in stack:
                        stack.pop()
                        break
    path.append(end)
    p = {}
    cell = end
    while cell != start:
        p[dfs[cell]] = cell 
        cell = dfs[cell]
    final = list(p.values())
    final.append(start)
    finalPath = final[::-1]
    return finalPath

def bfs_search(matrix, start, end):
    row = len(matrix)
    col = len(matrix[0])

    visited = [[False for i in range(col)]for j in range(row)]
    
    x = start[0]
    y = start[1]

    Dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    # Mark the source cell as visited
    visited[x][y] = True
    # Tao dictionary luu vi tri diem cha va diem con
    bfs = {}
    # Create a queue for BFS
    q = deque()

    q.append(start) #  Enqueue source cell

    # Do a BFS starting from source cell
    while q:
        curr = q.popleft() # Dequeue the front cell
        #path.append(curr)
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
                visited[a][b] = True
                q.append((a, b))
                bfs[(a,b)] = curr
    p = {}
    cell = end
    while cell != start:
        p[bfs[cell]] = cell 
        cell = bfs[cell]
    final = list(p.values())
    final.append(start)
    finalPath = final[::-1]
    return finalPath