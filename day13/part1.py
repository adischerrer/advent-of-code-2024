import datetime
import logging.config
import re


class XY:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __repr__(self):
        return f'{self.x}/{self.y}'


class ClawMachine:
    def __init__(self, a_move: XY, b_move: XY, prize_pos: XY) -> None:
        self.a_move: XY = a_move
        self.b_move: XY = b_move
        self.price_pos: XY = prize_pos

    def __repr__(self):
        return f'ButtonA:{self.a_move} ButtonB:{self.b_move} PricePos:{self.price_pos}'


def read_input() -> list[ClawMachine]:
    with open("input.txt", "r") as file:
        all_lines: list[str] = file.read().splitlines()

    button_pattern: re.Pattern[str] = re.compile(r'^Button [AB]: X\+(\d+), Y\+(\d+)$')
    prize_pattern: re.Pattern[str] = re.compile(r'^Prize: X=(\d+), Y=(\d+)$')
    result: list[ClawMachine] = []
    i: int = 0
    while i < len(all_lines):
        button_a_match = re.match(button_pattern, all_lines[i])
        a_move_x: int = int(button_a_match.group(1))
        a_move_y: int = int(button_a_match.group(2))
        button_b_match = re.match(button_pattern, all_lines[i + 1])
        b_move_x: int = int(button_b_match.group(1))
        b_move_y: int = int(button_b_match.group(2))
        prize_match = re.match(prize_pattern, all_lines[i + 2])
        prize_pos_x: int = int(prize_match.group(1))
        prize_pos_y: int = int(prize_match.group(2))
        result.append(ClawMachine(XY(a_move_x, a_move_y), XY(b_move_x, b_move_y), XY(prize_pos_x, prize_pos_y)))
        i += 4
    return result


def find_solution(cm: ClawMachine) -> tuple[int, int] | None:
    # Button B is cheaper (1 token) than the button A (3 tokens) => Prefer button B.
    max_kp_b: int = min(cm.price_pos.x // cm.b_move.x, cm.price_pos.y // cm.b_move.y)

    for kp_b in range(max_kp_b, 0, -1):
        kp_a_x: int = (cm.price_pos.x - kp_b * cm.b_move.x) // cm.a_move.x
        kp_a_y: int = (cm.price_pos.y - kp_b * cm.b_move.y) // cm.a_move.y
        if kp_a_x == kp_a_y:
            kp_a: int = kp_a_x
            if (kp_a * cm.a_move.x + kp_b * cm.b_move.x == cm.price_pos.x) and \
                    (kp_a * cm.a_move.y + kp_b * cm.b_move.y == cm.price_pos.y):
                return kp_a, kp_b
    return None


def main():
    claw_machines: list[ClawMachine] = read_input()
    total_prize: int = 0
    for i in range(len(claw_machines)):
        cm = claw_machines[i]
        keypress_counter: tuple[int, int] | None = find_solution(cm)
        if keypress_counter is None:
            logger.info(f'{i + 1:3}. {cm}: No solution found.')
        else:
            prize: int = keypress_counter[0] * 3 + keypress_counter[1]
            logger.info(f'{i + 1:3}. {cm}: Solution={keypress_counter}  Prize={prize}')
            total_prize += prize
    logger.info(f'Total prize: {total_prize}')


if __name__ == '__main__':
    logging.config.fileConfig('../log.conf')
    logger = logging.getLogger(__name__)

    start_time = datetime.datetime.now()
    main()
    logger.info('Execution time: {}'.format(datetime.datetime.now() - start_time))
