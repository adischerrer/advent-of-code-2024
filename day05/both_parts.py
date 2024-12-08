def parse_rule_line(line: str) -> tuple[int, int]:
    pages: list[str] = line.rstrip('\n').split('|')
    return int(pages[0]), int(pages[1])


def parse_page_input_line(line: str) -> list[int]:
    pages: list[int] = []
    for p in line.rstrip('\n').split(','):
        pages.append(int(p))
    return pages


def print_rules(rules: list[tuple[int, int]]) -> None:
    for index, rule in enumerate(rules):
        print(f'Rule {(index + 1):-4}: {rule}')


def sort_pages(pages: list[int], rules: list[tuple[int, int]]) -> list[int]:
    sorted_pages: list[int] = []
    for i in range(len(pages)):
        page: int = pages[i]
        insert_pos: int | None = None
        for j in range(len(sorted_pages)):
            try:
                # In case there is not rule, a ValueError occurs.
                _ = rules.index((page, sorted_pages[j])) >= 0
                insert_pos = j
                break
            except ValueError:
                pass  # Ignore. No rule found
        if insert_pos is not None:
            sorted_pages.insert(insert_pos, page)
        else:
            sorted_pages.append(page)
    return sorted_pages


def main() -> None:
    rules: list[tuple[int, int]] = []
    pages_input: list[list[int]] = []

    with open('input.txt', 'r') as file:
        for line in file:
            if line.find('|') != -1:
                rule: tuple[int, int] = parse_rule_line(line)
                rules.append(rule)
            elif line.find(',') != -1:
                pages: list[int] = parse_page_input_line(line)
                pages_input.append(pages)
    print_rules(rules)

    correct_middle_page_sum: int = 0
    incorrect_middle_page_sum: int = 0
    for pages in pages_input:
        pages_sorted = sort_pages(pages, rules)
        middle_index: int = int(len(pages_sorted) / 2)
        correct_order: bool = pages == pages_sorted
        if correct_order:
            correct_middle_page_sum += pages_sorted[middle_index]
        else:
            incorrect_middle_page_sum += pages_sorted[middle_index]
        print(f'Input:{pages}  -  Sorted:{pages_sorted}  -  Middle:{pages_sorted[middle_index]}  -  Correct order:{correct_order}')

    print(f'Sum of the middle pages of correct input: {correct_middle_page_sum}')
    print(f'Sum of the middle pages of incorrect input: {incorrect_middle_page_sum}')


if __name__ == '__main__':
    main()
