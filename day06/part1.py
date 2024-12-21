from __future__ import annotations

FREE_MARKER = '.'
OBSTRUCTED_MARKER = '#'
START_MARKER = '^'
VISITED_MARKER = 'X'


class Direction:
    def __init__(self, name: str, dx: int, dy: int, right_direction: Direction | None):
        self.name = name
        self.dx = dx
        self.dy = dy
        self.right_direction = right_direction

    def turn_right(self) -> Direction:
        return self.right_direction


class Field:
    def __init__(self):
        self.is_obstructed: bool = False
        self.is_start = False
        self.visit_count: int = 0

    def __repr__(self) -> str:
        if self.is_start:
            return START_MARKER
        elif self.is_obstructed:
            return OBSTRUCTED_MARKER
        elif self.visit_count > 0:
            return VISITED_MARKER
        else:
            return FREE_MARKER


class Area:
    FIELD_SIZE: int = 10

    def __init__(self):
        self.fields: list[list[Field]] = [[Field() for _ in range(self.FIELD_SIZE)] for _ in range(self.FIELD_SIZE)]

    def __repr__(self) -> str:
        result = ''
        for y in range(self.FIELD_SIZE):
            for x in range(self.FIELD_SIZE):
                result += self.field(x, y).__repr__()
            result += '\n'
        return result

    def field(self, x: int, y: int) -> Field:
        return self.fields[y][x]  # Attention: y is first index!

    def find_start(self) -> tuple[int, int]:
        for y in range(self.FIELD_SIZE):
            for x in range(self.FIELD_SIZE):
                if self.field(x, y).is_start:
                    return x, y

    def next_field_allowed(self, x: int, y: int, direction: Direction) -> bool:
        return 0 <= (x + direction.dx) < self.FIELD_SIZE and 0 <= (y + direction.dy) < self.FIELD_SIZE and \
            not self.field(x + direction.dx, y + direction.dy).is_obstructed

    def walk(self, x: int, y: int, heading: Direction) -> None:
        self.field(x, y).visit_count += 1
        while True:
            if self.field(x, y).visit_count > 4:
                return  # We already walked this path. One field can be crossed in 4 directions.
            while self.next_field_allowed(x, y, heading):
                x += heading.dx
                y += heading.dy
                self.field(x, y).visit_count += 1
            print(f'Position: {x=} {y=} {heading.name=}')

            if self.next_field_allowed(x, y, heading.right_direction):
                # Turn right
                heading = heading.turn_right()
            else:
                return  # Finish the walk

    def visited_fields(self) -> int:
        counter: int = 0
        for y in range(self.FIELD_SIZE):
            for x in range(self.FIELD_SIZE):
                counter += self.field(x, y).visit_count > 0
        return counter


def read_input(area):
    with open('input.txt', 'r') as file:
        y: int = 0
        for line in file:
            for x, char in enumerate(line.rstrip('\n')):
                area.field(x, y).is_obstructed = (char == OBSTRUCTED_MARKER)
                area.field(x, y).is_start = (char == START_MARKER)
            y += 1


def main() -> None:
    north: Direction = Direction("North", 0, -1, None)
    west: Direction = Direction("West", -1, 0, north)
    south: Direction = Direction("South", 0, 1, west)
    east: Direction = Direction("East", 1, 0, south)
    north.right_direction = east  # Must be set again

    area: Area = Area()
    read_input(area)
    print(f'{area}')

    x, y = area.find_start()
    area.walk(x, y, north)
    print(f'{area}')

    print(f'{area.visited_fields()} of the fields were visited')  # Returns 5020 which is wrong


if __name__ == '__main__':
    main()
