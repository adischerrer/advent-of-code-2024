import time
from typing import Final

INPUT_FILE: Final[str] = 'input_example1.txt'


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
                char = '.'
            print(char, end='')
        print()


def get_possible_directions(maze: Maze, pos: tuple[int, int]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x: int = pos[0] + direction[0]
        y: int = pos[1] + direction[1]
        if not maze.get_pos(x, y).is_wall and not maze.get_pos(x, y).is_path:
            result.append(direction)
    return result


def is_valid_state(maze: Maze, pos: tuple[int, int]) -> bool:
    # check if it is a valid solution
    return pos == maze.end_pos


def search(maze: Maze, pos: tuple[int, int]) -> bool:
    if is_valid_state(maze, pos):
        return True

    # find candidates for the next move
    for direction in get_possible_directions(maze, pos):
        x: int = pos[0] + direction[0]
        y: int = pos[1] + direction[1]
        new_pos = x,y
        maze.get_pos(x, y).is_path = True
        is_solved = search(maze, new_pos)
        if is_solved:
            return True
        else:
            maze.get_pos(x, y).is_path = False
    # None of the candidates solved the problem
    return False


def main():
    maze: Maze = read_input_maze()
    print_maze(maze)
    search(maze, maze.start_pos)
    print_maze(maze)
    print(f'Result: {0}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.03f}s')
