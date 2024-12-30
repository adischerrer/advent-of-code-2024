import time


def read_input() -> list[int]:
    with open("input.txt", "r") as file:
        stones: list[str] = file.read().split(' ')
    return list(map(int, stones))


def count_stones(stones: dict[int, int]) -> int:
    total: int = 0
    for s in stones.values():
        total += s
    return total


def blink(stones: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for stone, count in stones.items():
        num_length: int = len(str(stone))
        if stone == 0:
            inset_update_stones(result, 1, count)
        elif num_length % 2 == 0:
            inset_update_stones(result, int(str(stone)[0:num_length // 2]), count)
            inset_update_stones(result, int(str(stone)[num_length // 2: num_length]), count)
        else:
            inset_update_stones(result, stone * 2024, count)
    return result


def inset_update_stones(stones: dict[int, int], stone: int, count: int) -> None:
    if stone in stones:
        stones[stone] += count
    else:
        stones[stone] = count


def main():
    stones_start: list[int] = read_input()
    stones: dict[int, int] = dict.fromkeys(stones_start, 1)
    print(f'Start:  Number of stones: {count_stones(stones)}')
    blinks: int = 75

    for b in range(1, blinks + 1):
        stones = blink(stones)
        print(f'Blink {b:2}:  Number of stones: {count_stones(stones):15}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.03f}s')
