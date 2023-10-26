from enum import Enum
directions = Enum('directions', ['LEFT', 'RIGHT', 'UP', 'DOWN'])

def move(direction: Enum) -> None:

    if not isinstance(direction, directions):
        raise ValueError("Direction not found!!!")

    print(f"Moving for {direction.name}")

move(directions.LEFT)
