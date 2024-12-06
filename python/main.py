from collections import defaultdict
import re

def problem_01(puzzle_input: str):
    fp = open(puzzle_input, "r")
    lines: list[str] = fp.readlines()
    fp.close()

    left, right = [], []

    for line in lines:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    result_A = sum([abs(left[i]-right[i]) for i in range(len(left))])

    frequency = defaultdict(int)

    for num in right: frequency[num] += 1

    result_B = sum([num * frequency[num] for n in set(left)])

    return result_A, result_B


def problem_02(puzzle_input: str = "../02.txt"):
    fp = open(puzzle_input, "r")
    matrix = [ 
        [int(num) for num in line.split(' ')]
        for line in fp.readlines()
    ]
    
    result_A, result_B = 0, 0
    
    def safety(line: list[int]) -> bool:
        increasing = line[0] < line[1]
        
        for i in range(1, len(line)):
            diff = line[i] - line[i-1] if increasing else line[i-1] - line[i]
            if diff > 3 or diff < 1: return False     
        
        return True
    
    for report in matrix: 
        if safety(report): result_A += 1
    
    for report in matrix:
        if safety(report): 
            result_B += 1
            continue
        
        for i in range(len(report)):
            if safety(report[:i] + report[i+1:]):
                result_B += 1
                break
    
    return result_A, result_B
    

def problem_03(puzzle_input: str = "../03.txt"):
    REGEX = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    
    fp = open(puzzle_input, 'r')
    memory = fp.read()
    
    fp.close()
    
    result_A, result_B = 0, 0
    
    numbers = '1234567890'
    stages = ['', 'm', 'u', 'l', '(', numbers, ',', numbers, ')']
    num1, num2 = '', ''
    current = 0
    
    for i in range(len(memory)):
        
        # Attempt to move to next stage
        if memory[i] in stages[current+1]:
            current += 1
        else:
            # If `i` is not the next stage BUT belongs to one of the variable stages
            # Remain at current stage
            if (current == 5 or current == 7) and memory[i] in numbers: 
                current = current
            else:
                num1, num2 = '', ''
                # Move current stage back to 1 if its `m`
                if memory[i] == 'm': current = 1
                # Reset current stage otherwise    
                else: current = 0
            
        match current:
            case 8: result_A += int(num1) * int(num2); num1, num2 = '', ''; current = 0
            case 7: num1 += memory[i]
            case 5: num2 += memory[i]
            case _: pass
    
    memory: list[str] = re.findall(REGEX, memory)
    enabled = True
    
    for instruction in memory:
        match instruction:
            case "don't()": enabled = False
            case "do()": enabled = True
            case _: 
                if enabled:
                    num1, num2 = instruction[4:len(instruction)-1].split(',')
                    result_B += int(num1) * int(num2)
             
    print(result_B)        
    
    return result_A, result_B  
    

def problem_04(puzzle_input: str = "../04.txt"):
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
    

def problem_05(puzzle_input: str = "../05.txt"):
    result_A, result_B = 0, 0
    
    fp = open(puzzle_input, 'r')
    content = [line.replace('\n', '') for line in fp.readlines()]
    fp.close()
    
    destinations = defaultdict(set)
    origins = defaultdict(set)
    unqualified_updates = []
    
    reached_arrays = False
    
    for line in content:
        if line == '':
            reached_arrays = True
            continue
        
        if not reached_arrays:
            src, dest = line.split('|')
            destinations[int(src)].add(int(dest))
            origins[int(dest)].add(int(src))
        else:
            updates = [int(i) for i in line.split(',')]
            qualifies = True
            for i in range(len(updates)):
                before = origins[updates[i]].intersection(updates[:i]) if (i > 0) else set()
                after = destinations[updates[i]].intersection(updates[i+1:]) if (i < len(updates)-1) else set()
                
                if len(before) != len(updates[:i]) or len(after) != len(updates[i+1:]): 
                    qualifies = False
                    unqualified_updates.append(updates)
                    break
            
            result_A += updates[len(updates) // 2] if qualifies else 0
    
    for update in unqualified_updates:
        pass
    
     
    
    
    
    
    return result_A, result_B 

problem_05() 
        
