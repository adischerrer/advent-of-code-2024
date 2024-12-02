left: list[int] = []
right: list[int] = []

with open('input.txt', 'r') as file:
    for line in file:
        numbers: list[str] = line.split('   ')
        left.append(int(numbers[0].strip()))
        right.append(int(numbers[1].strip()))

    left.sort()
    right.sort()
    total_distance = 0

    for i in range(len(left)):
        print(f'{i=} {left[i]=} {right[i]=} | diff={abs(left[i] - right[i])}')
        total_distance += abs(left[i] - right[i])
    print(f'Total distance = {total_distance}')
