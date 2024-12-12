from collections import defaultdict


def template(puzzle_input: str) -> tuple[int]:
    result_A, result_B = 0, 0
   
    stream = open(puzzle_input, 'r').readline().replace('\n', '')
    blocks_A, blocks_B = [], []
    
    for i in range(len(stream)):
        if i % 2 == 0: blocks_A += [str(i // 2)] * int(stream[i])
        if i % 2 == 1: blocks_A += ['.'] * int(stream[i])    
    
    blocks_B = blocks_A.copy()
    
    l, r = 0, len(blocks_A)-1
    
    while l < r:
        if blocks_A[l] == '.':
            while blocks_A[r] == '.': r -= 1
            blocks_A[l] = blocks_A[r]
            blocks_A[r] = '.'    
        l += 1
        
    files = defaultdict(int)
    for c in blocks_B: 
        if c != '.': files[c] += 1
    
    files = [(k,v) for k,v in files.items()]
    
    for id in files[::-1]:
        l = 0
        while blocks_B[l] != id[0]:
            if blocks_B[l] != '.': 
                l += 1
                continue
            
            lb = l
            while blocks_B[lb] == '.': lb += 1
            if (lb-l) >= id[1]:
                blocks_B = blocks_B[:l] + [id[0]] * id[1] + blocks_B[l+id[1]:]
                times, r = id[1], len(blocks_B)-1
                while times > 0:
                    if blocks_B[r] == id[0]:
                        times -= 1
                        blocks_B[r] = '.'
                    r -= 1
                break    
            l = lb
            
            

    for i in range(len(blocks_A)):
        if blocks_A[i] != '.': result_A += int(blocks_A[i]) * i
        if blocks_B[i] != '.': result_B += int(blocks_B[i]) * i
    
    return result_A, result_B