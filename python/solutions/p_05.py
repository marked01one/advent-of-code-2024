from collections import defaultdict


def template(puzzle_input: str = "../05.txt"):
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