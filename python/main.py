from collections import defaultdict


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

    return [result_A, result_B]


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
    
    return [result_A, result_B]
    
    
    

problem_02()
        
