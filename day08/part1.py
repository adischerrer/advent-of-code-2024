class Pos:
    def __init__(self) -> None:
        self.freq = None
        self.is_antinode: bool = False

    def __repr__(self):
        return f'{"." if self.freq == None else self.freq}{"*" if self.is_antinode else " "}'


def read_input() -> list[list[Pos]]:
    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()

    size_x: int = len(lines[0])
    size_y: int = len(lines)
    area: list[list[Pos]] = [[Pos() for _ in range(size_x)] for _ in range(size_y)]

    for y in range(size_y):
        for x in range(size_x):
            if not lines[y][x] == '.':
                area[x][y].freq = lines[y][x]
    return area


def print_area(area: list[list[Pos]]) -> None:
    print()
    print('    ', end='')
    for x in range(len(area[0])):
        print(f'{x:02} ', end='')
    print()
    for y in range(len(area)):
        print(f'{y:2}  ', end='')
        for x in range(len(area[0])):
            print(f'{area[x][y]} ', end='')
        print()


def find_antinodes(area: list[list[Pos]]) -> None:
    min_x: int = 0
    max_x: int = len(area[0])
    min_y: int = 0
    max_y: int = len(area)

    for y1 in range(max_y):
        for x1 in range(max_x):
            for y2 in range(max_y):
                for x2 in range(max_x):
                    if not x1 == x2 and not y1 == y2 and \
                            not area[x1][y1].freq is None and \
                            area[x1][y1].freq == area[x2][y2].freq:
                        xa: int = x2 + x2 - x1
                        ya: int = y2 + y2 - y1
                        if min_x <= xa < max_x and min_y <= ya < max_y:
                            print(f'Check {x1},{y1} with {x2},{y2} => {xa},{ya}')
                            area[xa][ya].is_antinode = True
                        else:
                            print(f'Check {x1},{y1} with {x2},{y2} => out of area')


def count_antinodes(area: list[list[Pos]]) -> int:
    max_x: int = len(area[0])
    max_y: int = len(area)

    antinode_counter: int = 0
    for y in range(max_y):
        for x in range(max_x):
            if area[x][y].is_antinode:
                antinode_counter += 1
    return antinode_counter


def main():
    area: list[list[Pos]] = read_input()
    print_area(area)
    find_antinodes(area)
    print_area(area)
    print(f'Result: {count_antinodes(area)} antinodes found.')


if __name__ == '__main__':
    main()
