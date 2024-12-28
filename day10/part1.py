def read_input() -> list[list[int]]:
    with open("input.txt", "r") as file:
        all_lines: list[str] = file.read().splitlines()

    result: list[list[int]] = []
    for y, line in enumerate(all_lines):
        result.append([])
        for x, height in enumerate(line):
            result[y].append(int(height))
    return result


def print_trailmap(trailmap: list[list[int]]) -> None:
    for y in range(len(trailmap)):
        for x in range(len(trailmap[y])):
            print(trailmap[y][x], end='')
        print()


def is_valid_trail(trailmap: list[list[int]], x: int, y: int, expected: int) -> bool:
    return 0 <= y < len(trailmap) and 0 <= x < len(trailmap[y]) and trailmap[y][x] == expected


def find_trails(trailmap: list[list[int]], x: int, y: int, expected: int, solutions: set[tuple[int, int]]) -> None:
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if is_valid_trail(trailmap, x + dx, y + dy, expected):
            if expected == 9:
                solutions.add((x + dx, y + dy))
            find_trails(trailmap, x + dx, y + dy, expected + 1, solutions)


def count_trails(trailmap: list[list[int]], x: int, y: int) -> int:
    trail_ends: set[tuple[int, int]] = set()
    find_trails(trailmap, x, y, 1, trail_ends)
    return len(trail_ends)


def main():
    trailmap: list[list[int]] = read_input()
    print_trailmap(trailmap)
    trails_sum: int = 0
    for y in range(len(trailmap)):
        for x in range(len(trailmap[y])):
            if trailmap[y][x] == 0:
                trails_sum += count_trails(trailmap, x, y)
    print(f'Sum of trails: {trails_sum}')


if __name__ == '__main__':
    main()
