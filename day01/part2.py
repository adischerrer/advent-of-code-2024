left: list[int] = []
right: list[int] = []

with open('input.txt', 'r') as file:
    for line in file:
        numbers: list[str] = line.split('   ')
        left.append(int(numbers[0].strip()))
        right.append(int(numbers[1].strip()))

    left.sort()
    right.sort()
    similarity = 0
    total_similarity = 0

    for l in range(len(left)):
        hits = 0
        for r in range(len(right)):
            if left[l] == right[r]:
                hits += 1
        similarity = left[l] * hits
        print(f'{l=} {left[l]=} {hits=} | sim={similarity}')
        total_similarity += similarity
    print(f'Total similarity = {total_similarity}')
