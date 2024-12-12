from dataclasses import dataclass
from enum import Enum
from typing import Iterable

@dataclass
class Coord:
    x: int
    y: int

class Directions:
    def __init__(self):
        self.UP = Coord(-1, 0)
        self.DOWN = Coord(1, 0)
        self.LEFT = Coord(0, -1)
        self.RIGHT = Coord(0, 1)
    
    def __iter__(self): 
        for x in [self.UP, self.DOWN, self.LEFT, self.RIGHT]:
            yield x

 
class Vector():
    def __init__(self, src: tuple[int] | Iterable[tuple[int]], dest: tuple[int] | None = None):
        self.src: tuple[int] = src if dest else src[0]
        self.dest: tuple[int] = dest if dest else src[1]
        self.dir = self.__set_direction()
            
    def __str__(self) -> str: 
        return str((self.src, self.dest))
    
    def __set_direction(self) -> tuple[int]:
        return (self.__diff(self.src[0], self.dest[0]), self.__diff(self.src[1], self.dest[1]))
                
    def __diff(self, x1: int, x2: int) -> int: 
        return 0 if x1 == x2 else (x2-x1) // abs(x2-x1)

    def to_tuple(self) -> tuple[tuple[int]]:
        return (self.src, self.dest)
    
    
 
