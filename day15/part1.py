import time
from typing import Final

INPUT_FILE: Final[str] = 'input_example1.txt'


class Pos:
    def __init__(self) -> None:
        self.is_box = False
        self.is_wall = False


class Maze:
    def __init__(self, lines: list[str]) -> None:
        size_y: int = len(lines)
        size_x: int = len(lines[0])
        self.pos: list[list[Pos]] = [[Pos() for _ in range(size_x)] for _ in range(size_y)]
        for y in range(size_y):
            for x in range(size_x):
                if lines[y][x] == '#':
                    self.get_pos(x, y).is_wall = True
                elif lines[y][x] == 'O':
                    self.get_pos(x, y).is_box = True
                elif lines[y][x] == '@':
                    self.robot_pos = (x, y)

    def get_pos(self, x: int, y: int) -> Pos:
        return self.pos[y][x]  # Attention: y is first index!


def read_input_maze() -> Maze:
    maze_lines: list[str] = []
    with open(INPUT_FILE, 'r') as file:
        for l in file.read().splitlines():
            if l.startswith('#'):
                maze_lines.append(l)
    return Maze(maze_lines)


def read_input_moves() -> str:
    move_lines: list[str] = []
    with open(INPUT_FILE, 'r') as file:
        for l in file.read().splitlines():
            if not l.startswith('#'):
                move_lines.append(l)
    return ''.join(move_lines)


def print_maze(maze: Maze) -> None:
    for y in range(len(maze.pos)):
        for x in range(len(maze.pos[0])):
            char: str = '.'
            if maze.get_pos(x, y).is_wall:
                char = '#'
            elif maze.get_pos(x, y).is_box:
                char = 'O'
            elif maze.robot_pos == (x, y):
                char = '@'
            print(char, end='')
        print()


def calc_coord(maze: Maze) -> int:
    return 0


def main():
    maze: Maze = read_input_maze()
    print(f'Moves: {read_input_moves()}')
    print_maze(maze)
    print(f'GPS coordinates: {calc_coord(maze)}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.03f}s')
