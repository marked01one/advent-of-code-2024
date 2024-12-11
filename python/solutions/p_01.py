from collections import defaultdict


def template(puzzle_input: str) -> tuple[int]:
    fp = open(puzzle_input, "r")
    lines: list[str] = fp.readlines()
    fp.close()

    left, right = [], []

    for line in lines:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    result_A = sum([abs(left[i]-right[i]) for i in range(len(left))])

    frequency = defaultdict(int)

    for num in right: frequency[num] += 1

    result_B = sum([num * frequency[num] for n in set(left)])

    return result_A, result_B