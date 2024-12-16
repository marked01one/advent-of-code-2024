from collections import defaultdict
import re


def template(puzzle_input: str) -> tuple[int]:
    REGEX = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    numbers = "0123456789"
   
    
    fp = open(puzzle_input, 'r')
    memory = fp.read()
    
    fp.close()
    
    result_A, result_B = 0, 0
    
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
            if (current == 5 or current == 7) and memory[i].isnumeric(): 
                current = current
            else:
                num1, num2 = '', ''
                # Move current stage back to 1 if its `m`
                # Reset current stage otherwise    
                current = memory[i] == 'm'
                
            
        match current:
            case 8: result_A += int(num1) * int(num2); num1, num2 = '', ''; current = 0
            case 7: num1 += memory[i]
            case 5: num2 += memory[i]
            case _: pass
    
    memory: list[str] = re.findall(REGEX, memory)
    enabled = True
   
    
    for instruction in memory:
        if instruction == "don't()": enabled = False; continue
        if instruction == "do()": enabled = True; continue
        
        num1, num2 = instruction[4:len(instruction)-1].split(',')
        result_B += (int(num1) * int(num2)) * enabled    
    
             
    
    return result_A, result_B  