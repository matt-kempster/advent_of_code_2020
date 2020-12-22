from pathlib import Path
from typing import List, Dict


def main():
    contents = Path("./inputs/p22.txt").read_text()
    stacks: Dict[int, List[int]] = {1: [], 2: []}
    curr_player = 0
    for line in contents.split("\n"):
        if line.startswith("Player 1:"):
            curr_player = 1
        elif line.startswith("Player 2:"):
            curr_player = 2
        elif line.strip() == "":
            continue
        else:
            stacks[curr_player].append(int(line.strip()))
    while len(stacks[1]) != 0 and len(stacks[2]) != 0:
        play_round(stacks)

    print(score(stacks[1]) or score(stacks[2]))


def play_round(stacks: Dict[int, List[int]]):
    stack_1 = stacks[1]
    stack_2 = stacks[2]
    if stack_1[0] > stack_2[0]:
        stack_1 = stack_1[1:] + [stack_1[0], stack_2[0]]
        stack_2 = stack_2[1:]
    else:
        stack_2 = stack_2[1:] + [stack_2[0], stack_1[0]]
        stack_1 = stack_1[1:]
    stacks[1] = stack_1
    stacks[2] = stack_2

def score(stack: List[int]) -> int:
    return sum((len(stack) - i) * card for i, card in enumerate(stack))

if __name__ == "__main__":
    main()
