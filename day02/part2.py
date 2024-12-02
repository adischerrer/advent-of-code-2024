import math


def is_report_valid(rep: list[int]):
    last_direction = None
    for index in range(1, len(rep)):
        diff: int = rep[index] - rep[index - 1]
        if diff < -3 or diff == 0 or diff > 3:
            return False
        current_direction = math.copysign(1, diff)
        if last_direction is not None and last_direction != current_direction:
            return False
        last_direction = current_direction
    return True


def is_report_with_dumpener_valid(rep: list[int]):
    for i in range(len(rep)):
        reduced_rep = rep[:i] + rep[i + 1:]
        if is_report_valid(reduced_rep):
            return True
    return False


def main():
    reports: list[list[int]] = []

    with open('input.txt', 'r') as file:
        for line in file:
            strings: list[str] = line.split(' ')
            numbers: list[int] = []
            for i in range(len(strings)):
                numbers.append(int(strings[i].strip()))
            reports.append(numbers)

    valid_report_counter = 0

    for rep in reports:
        valid: bool = is_report_with_dumpener_valid(rep)
        print(rep, valid)
        if valid:
            valid_report_counter += 1

    print(f'Number of valid reports = {valid_report_counter}')


if __name__ == '__main__':
    main()
