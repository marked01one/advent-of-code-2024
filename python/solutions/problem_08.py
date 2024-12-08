from collections import defaultdict


def template(puzzle_input: str) -> tuple[int]:
    matrix = [line.replace('\n', '') for line in open(puzzle_input, 'r').readlines()]
    result_A, result_B = 0, 0
    
    # WRITE YOUR SOLUTION HERE
    antinode_table_A = [['.'] * len(line) for line in matrix]
    antinode_table_B = [['.'] * len(line) for line in matrix]
    m, n = len(antinode_table_A), len(antinode_table_A[0])
    
    tracker = defaultdict(list)
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != '.':
                tracker[matrix[i][j]].append((i,j))
                antinode_table_B[i][j] = '#'
                result_B += 1
                
    
    for value in tracker.values():
        for u in range(len(value)):
            for v in range(len(value)):
                if u == v: continue
                vec = (value[v][0]-value[u][0], value[v][1]-value[u][1])
                antinode = (value[v][0]+vec[0], value[v][1]+vec[1])
                
                cycle = 1
                while True:
                    if (antinode[0] < 0 or antinode[0] >= m): break
                    if (antinode[1] < 0 or antinode[1] >= n): break
                
                    if cycle == 1 and antinode_table_A[antinode[0]][antinode[1]] == '.':
                        antinode_table_A[antinode[0]][antinode[1]] = '#'
                        result_A += 1
                        
                    if antinode_table_B[antinode[0]][antinode[1]] == '.':
                        antinode_table_B[antinode[0]][antinode[1]] = '#'
                        result_B += 1
                    
                    antinode = (antinode[0]+vec[0], antinode[1]+vec[1])
                    cycle += 1
    
    
    
    return result_A, result_B 
    