from collections import defaultdict


def template(puzzle_input: str) -> tuple[int]:
    fp = open(puzzle_input, 'r')
    matrix = fp.readlines()
    
    result_A, result_B = 0, 0
    
    Xcoords, XMAScoords = [], []
    
    def is_xmas(line): return 1 if ''.join(line) == 'XMAS' else 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X': Xcoords.append((i, j))
    
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            if matrix[i][j] == 'A':
                XMAScoords.append((i, j))
    
    for x, y in Xcoords:
        N = is_xmas([matrix[x-i][y] for i in range(4)]) if x >= 3 else 0
        S = is_xmas([matrix[x+i][y] for i in range(4)]) if (x <= len(matrix)-4) else 0 
        W = is_xmas([matrix[x][y-j] for j in range(4)]) if (y >= 3) else 0
        E = is_xmas([matrix[x][y+j] for j in range(4)]) if (y <= len(matrix)-4) else 0
        
        NW = is_xmas([matrix[x-i][y-i] for i in range(4)]) if (x >= 3 and y >= 3) else 0
        NE = is_xmas([matrix[x-i][y+i] for i in range(4)]) if (x >= 3 and y <= len(matrix)-4) else 0
        SW = is_xmas([matrix[x+i][y-i] for i in range(4)]) if (x <= len(matrix)-4 and y >= 3) else 0
        SE = is_xmas([matrix[x+i][y+i] for i in range(4)]) if (x <= len(matrix)-4 and y <= len(matrix)-4) else 0
        
        result_A += sum([N, S, W, E, NW, NE, SW, SE])
    
    
    for x, y in XMAScoords:
        corners = matrix[x-1][y-1], matrix[x-1][y+1], matrix[x+1][y-1], matrix[x+1][y+1]
        
        if 'M' in corners and 'S' in corners and 'X' not in corners and 'A' not in corners:
            if corners[0] == corners[1] and corners[0] != corners[2] and corners[1] != corners[3]:
                result_B += 1
            elif corners[0] == corners[2] and corners[0] != corners[1] and corners[0] != corners[3]:
                result_B += 1 
        
    
    return result_A, result_B
    