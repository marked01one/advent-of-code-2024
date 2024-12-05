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
    

problem_03()
        
