import enum
from typing import List, Tuple
import numpy as np


class Directions(enum.Enum):
    up = 1
    down = 2    
    left = 3
    right = 4


def mover(direction: Directions | str) -> tuple:

    if not isinstance(direction, (Directions, str)):
        raise ValueError("Invalid direction")
    
    if direction == Directions.up or direction == 'up':
        return 0, 1    
    elif direction == Directions.down or direction == 'down':
        return 0, -1
    elif direction == Directions.left or direction == 'left':
        return -1, 0
    elif direction == Directions.right or direction == 'right':
        return 1, 0


def main():
    print(mover(Directions['up']))
    print(mover(Directions.right))
    print(mover(Directions(3).name))
    print(mover(Directions.down))


if __name__ == '__main__':
    main()
