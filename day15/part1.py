import time
from typing import Final

INPUT_FILE: Final[str] = 'input.txt'


class Pos:
    def __init__(self) -> None:
        self.is_box = False
        self.is_wall = False


class Maze:
    def __init__(self, lines: list[str]) -> None:
        self.size_y: int = len(lines)
        self.size_x: int = len(lines[0])
        self.pos: list[list[Pos]] = [[Pos() for _ in range(self.size_x)] for _ in range(self.size_y)]
        for y in range(self.size_y):
            for x in range(self.size_x):
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


def get_direction(char: str) -> tuple[int, int]:
    match char:
        case '>':
            return 1, 0
        case 'v':
            return 0, 1
        case '<':
            return -1, 0
        case _:
            return 0, -1


def find_space(maze: Maze, direction_char: str) -> tuple[int, int] | None:
    direction: tuple[int, int] = get_direction(direction_char)
    step: int = 0
    while True:
        step += 1
        check_pos = maze.robot_pos[0] + step * direction[0], maze.robot_pos[1] + step * direction[1]
        if maze.get_pos(check_pos[0], check_pos[1]).is_wall:
            return None
        elif not maze.get_pos(check_pos[0], check_pos[1]).is_box:
            return check_pos


def move_boxes(maze: Maze, space_pos: tuple[int, int]) -> None:
    # Move all boxes between robot and space_pos towards space_pos
    if not space_pos[0] == maze.robot_pos[0]:
        x_dir: int = 1 if space_pos[0] < maze.robot_pos[0] else -1
        y: int = space_pos[1]
        for x in range(space_pos[0], maze.robot_pos[0], x_dir):
            if maze.get_pos(x + x_dir, y).is_box:
                maze.get_pos(x + x_dir, y).is_box = False
                maze.get_pos(x, y).is_box = True
            if maze.robot_pos == (x + x_dir, y):
                maze.robot_pos = (x, y)
    if not space_pos[1] == maze.robot_pos[1]:
        y_dir: int = 1 if space_pos[1] < maze.robot_pos[1] else -1
        x: int = space_pos[0]
        for y in range(space_pos[1], maze.robot_pos[1], y_dir):
            if maze.get_pos(x, y + y_dir).is_box:
                maze.get_pos(x, y + y_dir).is_box = False
                maze.get_pos(x, y).is_box = True
            if maze.robot_pos == (x, y + y_dir):
                maze.robot_pos = (x, y)


def calc_coord(maze: Maze) -> int:
    coord_total = 0
    for x in range(maze.size_x):
        for y in range(maze.size_y):
            if maze.get_pos(x, y).is_box:
                coord_total += x + 100 * y
    return coord_total


def main():
    maze: Maze = read_input_maze()
    moves: str = read_input_moves()
    print(f'Moves: {read_input_moves()}')
    print_maze(maze)
    for move in moves:
        space_pos = find_space(maze, move)
        if space_pos is not None:
            move_boxes(maze, space_pos)
    print_maze(maze)
    print(f'GPS coordinates: {calc_coord(maze)}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.03f}s')
