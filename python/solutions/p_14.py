from collections import defaultdict
from PIL import Image
import numpy as np
import os


def template(puzzle_input: str, m: int, n: int):
    result_A, result_B = 0, 0
    
    
    lines = [
        line.replace('\n', '').split(' ')
        for line in open(puzzle_input, 'r').readlines()
    ]
    robots = [
        (line[0][2:].split(','), line[1][2:].split(','))
        for line in lines      
    ]
    
    cycles = 10000
    matrix = [[0] * n for _ in range(m)]
    
    robots = [
        (int(r[0][0]), int(r[0][1]), int(r[1][0]), int(r[1][1]))
        for r in robots
    ]
    
    
    
    for i in range(cycles):
        for j in range(len(robots)):
            px, py, vx, vy = robots[j]

            if i > 0: matrix[px][py] -= 1
                
            pxi = px+vx
            pxi = pxi+m if pxi < 0 else pxi
            pxi = pxi-m if pxi >= m else pxi

            pyi = py+vy
            pyi = pyi+n if pyi < 0 else pyi
            pyi = pyi-n if pyi >= n else pyi

            matrix[pxi][pyi] += 1
            robots[j] = (pxi, pyi, vx, vy)
        
        save_img(matrix, f"./outputs/frame_{i+1:05}.png")
    
    
    result_A = sum([sum(l[:(n//2)]) for l in matrix[:(m//2)]]) * \
        sum([sum(l[:(n//2)]) for l in matrix[(m//2)+1:]]) * \
        sum([sum(l[(n//2)+1:]) for l in matrix[:(m//2)]]) * \
        sum([sum(l[(n//2)+1:]) for l in matrix[(m//2)+1:]])
    
    frames = [(f, os.path.getsize(f"./outputs/{f}")) for f  in os.listdir("./outputs")]
    frames.sort(key= lambda x: x[1])
    result_B = int(frames[0][0].replace('frame_', '').replace('.png', ''))
    
    for frame in frames: os.remove(f"./outputs/{frame[0]}")
    
    return result_A, result_B


def save_img(mat: list[list[int]], path: str):
    img = Image.fromarray(np.array(mat, dtype=np.uint8) * 255)
    img.save(path)