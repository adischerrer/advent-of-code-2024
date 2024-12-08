MAT_LENGTH: int = 140


def equals_xmas(c1: str, c2: str, c3: str, c4: str, c5: str) -> bool:
    """
    c1 .. c2
    .. c3 ..
    c4 .. c5
    """
    return c3 == 'A' and \
        ((c1 == 'M' and c5 == 'S') or (c1 == 'S' and c5 == 'M')) and \
        ((c2 == 'M' and c4 == 'S') or (c2 == 'S' and c4 == 'M'))


def get_mat(v: int, h: int, mat) -> str | None:
    if v < 0 or v >= MAT_LENGTH or h < 0 or h >= MAT_LENGTH:
        return None
    return mat[v][h]


def is_xmas(v, h, mat) -> bool:
    return equals_xmas(get_mat(v, h, mat), get_mat(v, h + 2, mat), get_mat(v + 1, h + 1, mat), get_mat(v + 2, h, mat), get_mat(v + 2, h + 2, mat))


def main() -> None:
    mat: list[list[str]] = [['.' for i in range(MAT_LENGTH)] for i in range(MAT_LENGTH)]
    # print(f'{mat}')

    with open('input.txt', 'r') as file:
        v_index: int = 0
        for line in file:
            for h_index, char in enumerate(line.rstrip('\n')):
                mat[v_index][h_index] = char
            v_index += 1
    # print(f'{mat}')

    counter: int = 0
    for v_index in range(MAT_LENGTH):
        for h_index in range(MAT_LENGTH):
            if is_xmas(v_index, h_index, mat):
                counter += 1

    print(f'{counter} XMAS found')


if __name__ == '__main__':
    main()
