import datetime
import logging.config


class Block:
    def __init__(self, file_id: int | None) -> None:
        self.file_id: int = file_id
        self.is_free: bool = (file_id is None)

    def __repr__(self):
        if self.file_id is None:
            return '    .'
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
    for i, b in enumerate(disk):
        logger.debug(f'Pos: {i:-6}  {b}')
    logger.debug('=========================================================================')


def find_empty_space(disk: list[Block], size: int, max_pos: int) -> int | None:
    """
    Find first position containing an empty space of size.
    :param disk:
    :param size:
    :param max_pos: The empty space must be at a lower position.
    :return: position on disk or None in case no space is found.
    """
    i: int = 0
    while i < min(max_pos, len(disk)):
        start_pos: int = i
        check_pos = start_pos
        while disk[check_pos].is_free and check_pos < len(disk):
            if (check_pos - start_pos + 1) == size:
                return start_pos
            check_pos += 1
        i += 1
    return None


def file_info(disk: list[Block], file_id: int) -> tuple[int | None, int | None]:
    """
    Find the file by given file_id on the given disk. Return its position and size.
    :param disk:
    :param file_id:
    :return: a tuple(position, size) of file
    """
    position: int | None = None
    size: int | None = None
    for i in range(len(disk)):
        if disk[i].file_id == file_id:
            if position is None:
                position = i
                size = 1
            else:
                size += 1
    return position, size


def compact_disk(disk: list[Block]) -> None:
    max_file_id: int = 0
    for i in reversed(range(len(disk))):
        if not disk[i].file_id is None:
            max_file_id = disk[i].file_id
            break

    max_movable_file_size: int = 9
    for file_id in reversed(range(max_file_id + 1)):
        file_pos, file_size = file_info(disk, file_id)
        if file_size <= max_movable_file_size:  # Performance optimization
            pos_empty: int | None = find_empty_space(disk, file_size, file_pos)
            if not pos_empty is None:
                # Move file to new location
                logger.debug(f'Move {file_id=} with {file_size=} from {file_pos=} to {pos_empty=}')
                for i in range(file_size):
                    temp_empty: Block = disk[pos_empty + i]
                    disk[pos_empty + i] = disk[file_pos + i]
                    disk[file_pos + i] = temp_empty
            else:
                # File is too large to be moved.
                max_movable_file_size = file_size - 1
                if max_movable_file_size == 0:  # Performance optimization
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

    ''' Test helper methods
    for i in range(1, 10):
        print(f'First pos of {i=} size empty block: {find_empty_space(disk, i, 1000)}')
    for file_id in [22, 53, 123, 9999, 12345]:
        start, size = file_info(disk, file_id)
        print(f'Info for {file_id=} : {start=} and {size=}')
    '''

    compact_disk(disk)
    print_disk(disk)
    logger.info(f'Checksum = {calc_checksum(disk)}')


if __name__ == '__main__':
    logging.config.fileConfig('../log.conf')
    logger = logging.getLogger(__name__)

    start_time = datetime.datetime.now()
    main()
    logger.info('Execution time: {}'.format(datetime.datetime.now() - start_time))
