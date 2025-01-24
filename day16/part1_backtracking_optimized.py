import time
from typing import Final
import sys

sys.setrecursionlimit(10 ** 6)

INPUT_FILE: Final[str] = 'input.txt'


class Params:
    best_path: list[tuple[int, int]] = []
    best_cost: int = 0


class Pos:
    def __init__(self) -> None:
        self.is_wall = False
        self.is_path = False


class Maze:
    def __init__(self, lines: list[str]) -> None:
        self.size_y: int = len(lines)
        self.size_x: int = len(lines[0])
        self.pos: list[list[Pos]] = [[Pos() for _ in range(self.size_x)] for _ in range(self.size_y)]
        for y in range(self.size_y):
            for x in range(self.size_x):
                if lines[y][x] == '#':
                    self.get_pos(x, y).is_wall = True
                elif lines[y][x] == 'S':
                    self.get_pos(x, y).is_path = True
                    self.start_pos = (x, y)
                elif lines[y][x] == 'E':
                    self.end_pos = (x, y)

    def get_pos(self, x: int, y: int) -> Pos:
        return self.pos[y][x]  # Attention: y is first index!


def read_input_maze() -> Maze:
    with open(INPUT_FILE, 'r') as file:
        return Maze(file.read().splitlines())


def print_maze(maze: Maze) -> None:
    for y in range(len(maze.pos)):
        for x in range(len(maze.pos[0])):
            char: str = ' '
            if maze.start_pos == (x, y):
                char = 'S'
            elif maze.end_pos == (x, y):
                char = 'E'
            elif maze.get_pos(x, y).is_wall:
                char = '#'
            elif maze.get_pos(x, y).is_path:
                char = '+'
            print(char, end='')
        print()


def get_possible_directions(maze: Maze, pos: tuple[int, int], p_dir: tuple[int, int]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []

    # Prioritize directions - towards upper right corner
    directions: list[tuple[int, int]] = []
    if p_dir == (1, 0):
        directions = [(1, 0), (0, -1), (0, 1)]
    elif p_dir == (0, 1):
        directions = [(1, 0), (0, 1), (-1, 0)]
    elif p_dir == (-1, 0):
        directions = [(0, -1), (0, 1), (-1, 0)]
    else:
        directions = [(0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        x: int = pos[0] + direction[0]
        y: int = pos[1] + direction[1]
        if not maze.get_pos(x, y).is_wall:
            result.append(direction)
    return result


def search(maze: Maze, p_dir: tuple[int, int], p_cost: int, path: list[tuple[int, int]], params: Params) -> None:
    if path[-1] == maze.end_pos:
        if p_cost < params.best_cost or params.best_cost == 0:
            params.best_path = path.copy()
            params.best_cost = p_cost
            print(f'{time.time() - start_time:.03f}s - New best path: Cost: {params.best_cost}')
        return
    if not params.best_cost == 0 and p_cost > params.best_cost:
        return

    # find candidates for the next move
    for direction in get_possible_directions(maze, path[-1], p_dir):
        x: int = path[-1][0] + direction[0]
        y: int = path[-1][1] + direction[1]
        new_pos = x, y
        if new_pos in path:
            continue
        path.append(new_pos)
        if direction == p_dir:
            cost: int = p_cost + 1
        else:
            cost: int = p_cost + 1000
        search(maze, direction, cost, path, params)
        path.pop()


def main():
    maze: Maze = read_input_maze()
    print_maze(maze)
    current_direction: tuple[int, int] = (1, 0)
    current_cost: int = 0
    current_path: list[tuple[int, int]] = [maze.start_pos]
    params: Params = Params()
    search(maze, current_direction, current_cost, current_path, params)
    for path in params.best_path:
        maze.get_pos(path[0], path[1]).is_path = True
    print_maze(maze)
    print(f'Result: Cost: {params.best_cost}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.03f}s')
