from collections import defaultdict, deque


def template(puzzle_input: str) -> tuple[int]:
    result_A, result_B = 1, 0
    
    fp = open(puzzle_input, 'r')
    
    matrix = [list(line.replace('\n', '')) for line in fp.readlines()]
    
    def turn(x: int, y: int):
        if x == -1 and y == 0: return 0, 1
        if x == 0 and y == 1: return 1, 0
        if x == 1 and y == 0: return 0, -1
        if x == 0 and y == -1: return -1, 0
        
    
    guard = (-1, -1)
    direction = (-1, 0)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '^':
                guard = (i, j)
                break
    
    prev = deque([])
    pairs = set()
    loop_blocks = set()
            
    while (0 <= guard[0] and guard[0] < len(matrix)) and (0 <= guard[1] and guard[1] < len(matrix[0])):
        next = (guard[0]+direction[0], guard[1]+direction[1])
        
        if (0 <= next[0] and next[0] < len(matrix)) and (0 <= next[1] and next[1] < len(matrix[0])):
            if matrix[next[0]][next[1]] == '#': 
                prev.append(guard)
                if len(prev) > 2: prev.popleft()
                
                direction = turn(direction[0], direction[1])
                next = (guard[0]+direction[0], guard[1]+direction[1])
                
        if len(prev) == 2: pairs.add((prev[0], prev[1]))    
         
                
        
        if matrix[guard[0]][guard[1]] == '.': result_A += 1
        matrix[guard[0]][guard[1]] = 'X'    
        guard = next 
  
    result_B = len(loop_blocks)
    print(pairs)
   
    return result_A, result_B