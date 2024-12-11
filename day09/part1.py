class Block:
    def __init__(self, file_id: int | None) -> None:
        self.file_id: int = file_id
        self.is_free: bool = (file_id is None)

    def __repr__(self):
        if self.file_id is None:
            return ('    .')
        return f'{self.file_id:5}'


def read_input() -> list[Block]:
    with open("input.txt", "r") as file:
        diskmap: str = file.read().rstrip('\n')

    diskmap_length: int = len(diskmap)
    disk: list[Block] = []
    for i in range(diskmap_length):
        if i % 2 == 0:
            # File
            file_id: int = i // 2
            file_size: int = int(diskmap[i])
            for f in range(file_size):
                disk.append(Block(file_id))
        else:
            # Empty space
            file_size: int = int(diskmap[i])
            for f in range(file_size):
                disk.append(Block(None))
    return disk


def print_disk(disk: list[Block]) -> None:
    line: str = ''
    with open('console.log', 'w') as file:
        for i, b in enumerate(disk):
            line = f'Pos: {i:-6}  {b}'
            file.write(line + '\n')
            print(line)
        line = '========================================================================='
        file.write(line + '\n')
        print(line)


def compact_disk(disk: list[Block]) -> None:
    start: int = 0
    end: int = len(disk) - 1
    while True:
        while not disk[start].is_free:
            start += 1
        while disk[end].is_free:
            end -= 1
        if start < end:
            # Swap start with end Block
            temp_end: Block = disk[end]
            disk[end] = disk[start]
            disk[start] = temp_end
        else:
            break


def calc_checksum(disk: list[Block]) -> int:
    checksum: int = 0
    for i, b in enumerate(disk):
        if not b.file_id is None:
            checksum += i * b.file_id
    return checksum


def main():
    disk: list[Block] = read_input()
    print_disk(disk)
    compact_disk(disk)
    print_disk(disk)
    print(f'Checksum = {calc_checksum(disk)}')


if __name__ == '__main__':
    main()
