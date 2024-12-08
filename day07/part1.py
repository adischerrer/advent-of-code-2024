class MathQuiz:
    def __init__(self, result: int, numbers: list[int]) -> None:
        self.result: int = result
        self.numbers: list[int] = numbers

    def __repr__(self):
        return f'{self.result}  ?=  {" [ ] ".join(map(str, self.numbers))}'


def read_input() -> list[MathQuiz]:
    quiz: list[MathQuiz] = []
    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()
    for line in lines:
        left_str, right_str = line.split(":")
        result = int(left_str)
        numbers = list(map(int, right_str.split()))
        quiz.append(MathQuiz(result, numbers))
    return quiz


def find_solution(r: int, num: list[int]) -> bool:
    if len(num) == 1:
        return r == num[0]
    division_without_rest: bool = r % num[-1] == 0
    return find_solution(r - num[-1], num[:-1]) or (division_without_rest and find_solution(r // num[-1], num[:-1]))


def main():
    quiz: list[MathQuiz] = read_input()

    result_sum: int = 0
    for i, q in enumerate(quiz):
        solution_found: bool = find_solution(q.result, q.numbers)
        if solution_found:
            result_sum += q.result
        print(f'After equation {i:3}:  Total={result_sum:13}  {"OK" if solution_found else "--"}  {q}')

    print(f'Sum of results having a solution: {result_sum}')


if __name__ == '__main__':
    main()
