from collections import defaultdict, deque


def template(puzzle_input: str) -> tuple[int]:
    result_A, result_B = 0, 0
    stream = open(puzzle_input, 'r').readlines()
    matrix = [[int(i) for i in list(line.replace('\n', ''))] for line in stream]
    m, n = len(matrix), len(matrix[0])
    
    trailheads = defaultdict(set)
    
    
    queue = deque([])
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0: queue.append(((i, j), (i, j)))

    
    
    
    while queue:
        head, curr = queue.popleft()
        if  matrix[curr[0]][curr[1]] == 9:
            trailheads[head].add(curr)
            result_B += 1
            continue
        
        i, j = curr
        if i > 0 and matrix[i-1][j] == matrix[i][j]+1: queue.append((head, (i-1,j)))
        if i < m-1 and matrix[i+1][j] == matrix[i][j]+1: queue.append((head, (i+1,j)))
        if j > 0 and matrix[i][j-1] == matrix[i][j]+1: queue.append((head, (i,j-1)))
        if j < n-1 and matrix[i][j+1] == matrix[i][j]+1: queue.append((head, (i,j+1)))
    
    for end in trailheads.values(): result_A += len(end)
     
    return result_A, result_B