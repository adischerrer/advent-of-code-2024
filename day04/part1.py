MAT_LENGTH: int = 140


def equals_xmas(c1: str, c2: str, c3: str, c4: str) -> bool:
    return c1 == 'X' and c2 == 'M' and c3 == 'A' and c4 == 'S'


def get_mat(v: int, h: int, mat) -> str | None:
    if v < 0 or v >= MAT_LENGTH or h < 0 or h >= MAT_LENGTH:
        return None
    return mat[v][h]


def is_xmas(v, h, direction, mat) -> bool:
    try:
        match direction:
            case 0:  # Direction East
                return equals_xmas(get_mat(v, h, mat), get_mat(v, h + 1, mat), get_mat(v, h + 2, mat), get_mat(v, h + 3, mat))
            case 1:  # Direction South-East
                return equals_xmas(get_mat(v, h, mat), get_mat(v + 1, h + 1, mat), get_mat(v + 2, h + 2, mat), get_mat(v + 3, h + 3, mat))
            case 2:  # Direction South
                return equals_xmas(get_mat(v, h, mat), get_mat(v + 1, h, mat), get_mat(v + 2, h, mat), get_mat(v + 3, h, mat))
            case 3:  # Direction South-West
                return equals_xmas(get_mat(v, h, mat), get_mat(v + 1, h - 1, mat), get_mat(v + 2, h - 2, mat), get_mat(v + 3, h - 3, mat))
            case 4:  # Direction West
                return equals_xmas(get_mat(v, h, mat), get_mat(v, h - 1, mat), get_mat(v, h - 2, mat), get_mat(v, h - 3, mat))
            case 5:  # Direction North-West
                return equals_xmas(get_mat(v, h, mat), get_mat(v - 1, h - 1, mat), get_mat(v - 2, h - 2, mat), get_mat(v - 3, h - 3, mat))
            case 7:  # Direction North
                return equals_xmas(get_mat(v, h, mat), get_mat(v - 1, h, mat), get_mat(v - 2, h, mat), get_mat(v - 3, h, mat))
            case 6:  # Direction North-East
                return equals_xmas(get_mat(v, h, mat), get_mat(v - 1, h + 1, mat), get_mat(v - 2, h + 2, mat), get_mat(v - 3, h + 3, mat))
            case _:  # Default (should never be the case)
                return False
    except IndexError:
        return False


def main() -> None:
    mat: list[list[str]] = [['.' for i in range(MAT_LENGTH)] for i in range(MAT_LENGTH)]
    print(f'{mat}')

    with open('input.txt', 'r') as file:
        v_index: int = 0
        for line in file:
            for h_index, char in enumerate(line.rstrip('\n')):
                mat[v_index][h_index] = char
            v_index += 1
    print(f'{mat}')

    counter: int = 0
    for v_index in range(MAT_LENGTH):
        for h_index in range(MAT_LENGTH):
            for direction in range(8):
                if is_xmas(v_index, h_index, direction, mat):
                    counter += 1

    print(f'{counter} XMAS found')


if __name__ == '__main__':
    main()
