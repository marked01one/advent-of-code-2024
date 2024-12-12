from collections import defaultdict


def template(puzzle_input: str) -> tuple[int]:
    result_A, result_B = 0, 0
    
    fp = open(puzzle_input, 'r')
    
    for line in fp.readlines():
        key = int(line.split(':')[0])
        values = [int(i) for i in line.split(':')[1].strip().split(' ')]
        result_A += traverse_A(values, 0, 0, key) * key
        result_B += traverse_B(values, 0, 0, key) * key
    
    fp.close()
    
    return result_A, result_B


def traverse_A(arr, idx, total, target):
    if total > target: return False
    
    if idx == len(arr)-1: 
        if target == total + arr[idx]: return True
        return (target == total * arr[idx])
    
    if traverse_A(arr, idx+1, total+arr[idx], target): return True
    return traverse_A(arr, idx+1, total*arr[idx], target)

 
def traverse_B(arr, idx, total, target):
    if total > target: return False
    
    if idx == len(arr)-1:
        if target == total + arr[idx]: return True
        if target == total * arr[idx]: return True
        return target == int(str(total) + str(arr[idx]))
    
    if traverse_B(arr, idx+1, total+arr[idx], target): return True
    if traverse_B(arr, idx+1, total*arr[idx], target): return True
    return traverse_B(arr, idx+1, int(str(total)+str(arr[idx])), target)