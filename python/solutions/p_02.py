from collections import defaultdict


def template(puzzle_input: str = "../02.txt"):
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
        if safety(report):
            result_A += 1
            result_B += 1
            continue
        
        for i in range(len(report)):
            if safety(report[:i] + report[i+1:]):
                result_B += 1
                break
    
    return result_A, result_B