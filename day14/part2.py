import datetime
import logging.config
import re


class XY:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __repr__(self):
        return f'{self.x}/{self.y}'


class Robot:
    def __init__(self, pos: XY, dir: XY) -> None:
        self.pos: XY = pos
        self.dir: XY = dir

    def __repr__(self):
        return f'Pos:{self.pos}  Dir:{self.dir}'


def read_input() -> list[Robot]:
    with open("input.txt", "r") as file:
        robot_lines: list[str] = file.read().splitlines()

    pattern: re.Pattern[str] = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    robots: list[Robot] = []
    for i, line in enumerate(robot_lines):
        match = re.match(pattern, line)
        pos_x: int = int(match.group(1))
        pos_y: int = int(match.group(2))
        dir_x: int = int(match.group(3))
        dir_y: int = int(match.group(4))
        robots.append(Robot(XY(pos_x, pos_y), XY(dir_x, dir_y)))
    return robots


def print_area(title: str, area: list[list[int]]) -> None:
    logger.info(title)
    for y in range(len(area)):
        msg: str = ''
        for x in range(len(area[y])):
            msg += f'{"X" if area[y][x] > 0 else " "}'
        logger.info(msg)

def find_pattern(area: list[list[int]]) -> bool:
    msg: str = ''
    for y in range(len(area)):
        for x in range(len(area[y])):
            msg += f'{"X" if area[y][x] > 0 else " "}'
    return msg.find("XXXXXXXXXX") > 0

def main():
    size_x: int = 101
    size_y: int = 103
    time_factor: int = 10000
    area_start: list[list[int]] = [[0 for _ in range(size_x)] for _ in range(size_y)]

    robots: list[Robot] = read_input()
    for i in range(len(robots)):
        area_start[robots[i].pos.y][robots[i].pos.x] += 1
    print_area('Start', area_start)

    for t in range(time_factor):
        area_end: list[list[int]] = [[0 for _ in range(size_x)] for _ in range(size_y)]
        for i in range(len(robots)):
            end_x: int = (robots[i].pos.x + t * robots[i].dir.x) % size_x
            end_y: int = (robots[i].pos.y + t * robots[i].dir.y) % size_y
            area_end[end_y][end_x] += 1
        if find_pattern(area_end):
            print_area(f'Found pattern after {t=} steps', area_end)
            break


if __name__ == '__main__':
    logging.config.fileConfig('../log.conf')
    logger = logging.getLogger(__name__)

    start_time = datetime.datetime.now()
    main()
    logger.info('Execution time: {}'.format(datetime.datetime.now() - start_time))
