from collections import defaultdict


def template(puzzle_input: str) -> tuple[int]:
    result_A, result_B = 0, 0
    
    fp = open(puzzle_input, 'r')
    
    tracker = defaultdict(list)
    
    for line in fp.readlines():
        key = int(line.split(':')[0])
        values = [int(i) for i in line.split(':')[1].strip().split(' ')]
        tracker[key] = values
    
    fp.close()
    
    def traverse_A(arr, idx, total, target):
        if total > target: return False
        
        if idx == len(arr)-1: 
            add_val = total + arr[idx]
            mul_val = total * arr[idx]
            return (add_val == target) or (mul_val == target)
        else:
            add = traverse_A(arr, idx+1, total+arr[idx], target) 
            mul = traverse_A(arr, idx+1, total*arr[idx], target)
            return add or mul
    
    for k,v in tracker.items():
        if traverse_A(v, 0, 0, k): result_A += k
        

    def traverse_B(arr, idx, total, target):
        if total > target: return False
        
        if idx == len(arr)-1:
            add_val = total + arr[idx]
            mul_val = total * arr[idx]
            cat_val = int(str(total) + str(arr[idx]))
            return add_val == target or mul_val == target or cat_val == target
        else:
            add = traverse_B(arr, idx+1, total+arr[idx], target)
            mul = traverse_B(arr, idx+1, total*arr[idx], target)
            cat = traverse_B(arr, idx+1, int(str(total)+str(arr[idx])), target)
            return add or mul or cat
   
    for k, v in tracker.items():
        if traverse_B(v, 0 ,0, k): result_B += k
    
    print(result_B)
    
    return result_A, result_B