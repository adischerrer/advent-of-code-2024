def read_input() -> list[list[int]]:
    with open("input.txt", "r") as file:
        all_lines: list[str] = file.read().splitlines()

    result: list[list[int]] = []
    for y, line in enumerate(all_lines):
        result.append([])
        for x, height in enumerate(line):
            result[y].append(int(height))
    return result


def print_trail_map(trail_map: list[list[int]]) -> None:
    for y in range(len(trail_map)):
        for x in range(len(trail_map[y])):
            print(trail_map[y][x], end='')
        print()


def is_valid_trail(trail_map: list[list[int]], x: int, y: int, expected: int) -> bool:
    return 0 <= y < len(trail_map) and 0 <= x < len(trail_map[y]) and trail_map[y][x] == expected


def find_trails(trail_map: list[list[int]], x: int, y: int, expected: int, solutions: set[tuple[int, int]]) -> None:
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if is_valid_trail(trail_map, x + dx, y + dy, expected):
            if expected == 9:
                solutions.add((x + dx, y + dy))
            find_trails(trail_map, x + dx, y + dy, expected + 1, solutions)


def count_trails(trail_map: list[list[int]], x: int, y: int) -> int:
    trail_ends: set[tuple[int, int]] = set()
    find_trails(trail_map, x, y, 1, trail_ends)
    return len(trail_ends)


def main():
    trail_map: list[list[int]] = read_input()
    print_trail_map(trail_map)
    trail_counter: int = 0
    for y in range(len(trail_map)):
        for x in range(len(trail_map[y])):
            if trail_map[y][x] == 0:
                trail_counter += count_trails(trail_map, x, y)
    print(f'Number of trails: {trail_counter}')


if __name__ == '__main__':
    main()
