import time


def read_input() -> list[int]:
    with open("input.txt", "r") as file:
        stones: list[str] = file.read().split(' ')
    return list(map(int, stones))


def print_stones(stones: list[int]) -> None:
    for pos in range(len(stones)):
        print(stones[pos], end='  ')
    print()


def blink(stones: list[int]) -> list[int]:
    result: list[int] = []
    for stone in stones:
        num_length: int = len(str(stone))
        if stone == 0:
            result.append(1)
        elif num_length % 2 == 0:
            result.append(int(str(stone)[0:num_length // 2]))
            result.append(int(str(stone)[num_length // 2: num_length]))
        else:
            result.append(stone * 2024)
    return result


def main():
    blinks: int = 25
    stones: list[int] = read_input()
    print_stones(stones)
    for i in range(1, blinks + 1):
        stones = blink(stones)
        print(f'Blink {i:2}:  Number of stones: {len(stones):10}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.03f}s')
