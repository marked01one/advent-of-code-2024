from collections import defaultdict, deque


def template(puzzle_input: str) -> tuple[int]:
    file = open(puzzle_input, 'r').readlines()
    result_A, result_B = 0, 0
    
    # WRITE YOUR SOLUTION HERE
    plots = [list(line.replace('\n', '')) for line in file]
    matrix = [list(line.replace('\n', '')) for line in file]
    m, n = len(plots), len(plots[0])
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for i in range(m):
        for j in range(n):
            if plots[i][j] == '.': continue
            
            perimeter = 0
            curr, queue = matrix[i][j], deque([(i, j)])
            visited, edges = set(), defaultdict(list)
            corners = 0
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited: continue
                visited.add((x, y))
                
                l, neighbors = [], []
                
                for dx, dy in directions:
                    xi, yi = x+dx, y+dy
                    if (xi, yi) in visited: 
                        l.append(0)
                        neighbors.append(1)
                        continue
                    
                    edge = (yi < 0 or yi >= n) or (xi < 0 or xi >= m) or matrix[xi][yi] != curr
                    
                    perimeter += edge
                    l.append(edge)
                    neighbors.append(not edge)    
                        
                    if ((0 <= xi < m) and (0 <= yi < n) and matrix[xi][yi] == curr): queue.append((xi, yi))
                
                
                # Count corners
                for ii in range(4):
                    # Convex corners
                    if l[ii] + l[ii-1] == 2: corners += 1
                    # Concave corners
                    if neighbors[ii]+neighbors[ii-1] != 2: continue
                    xii, yii = (x+directions[ii][0]+directions[ii-1][0], y+directions[ii][1]+directions[ii-1][1])
                    if matrix[xii][yii] != curr: corners += 1
                
                
                plots[x][y] = '.'
            
            
            result_A += len(visited) * perimeter
            result_B += len(visited) * corners

    return result_A, result_B 
