import re


def main() -> None:
    mem: str = ''

    with open('input.txt', 'r') as file:
        for line in file:
            mem += line
    print(f'{mem}')

    total: int = 0
    enabled: bool = True
    matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', mem)

    for index, match in enumerate(matches):
        if match.group(0) == 'do()':
            enabled = True
        elif match.group(0) == 'don\'t()':
            enabled = False
        else:
            start_index: int = match.start()
            end_index: int = match.end()
            mul1: int = int(match.group(1))
            mul2: int = int(match.group(2))
            print(f'{index:-3}: mul1={mul1:3} mul2={mul2:3} mem[{start_index}..{end_index}]={mem[start_index:end_index]}) {enabled=}')
            if enabled:
                total += mul1 * mul2
    print(f'{total=}')


if __name__ == '__main__':
    main()
