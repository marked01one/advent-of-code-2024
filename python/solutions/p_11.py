from collections import defaultdict


def template(puzzle_input: str) -> tuple[int]:
    result_A, result_B = 0, 0
    
    stream = open(puzzle_input, 'r').read().replace('\n', '').split(' ')
    stream = [int(i) for i in stream]
    hashmap = defaultdict(int)
    
    for s in stream: hashmap[s] = 1
    next = tuple(hashmap.items())
   
    for i in range(75):
        if i == 25: result_A = sum(hashmap.values())
        
        items = tuple(hashmap.items())
        for num,_ in items: hashmap[num] = 0
        
        for num, val in items:
            if val == 0: continue

            if num == 0: hashmap[1] += val
            elif len(str(num)) % 2 == 0:
                strs = str(num)
                n = len(strs) // 2
                hashmap[num % (10**n)] += val
                hashmap[num // (10**n)] += val
            else:
                hashmap[num * 2024] += val
    
    
    result_B = sum(hashmap.values())
        
    
    return result_A, result_B