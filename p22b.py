from pathlib import Path
from typing import List, Dict, Set, Tuple
from sys import argv
from ast import literal_eval

def main():
    if len(argv) != 1:
        stacks = literal_eval(argv[1])
    else:
        stacks = get_stacks()
    play_game(stacks)
    print(score(stacks[1]) or score(stacks[2]))

def get_stacks() -> Dict[int, List[int]]:
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
    return stacks


def play_game(stacks: Dict[int, List[int]]) -> int:
    seen_stacks: Set[Tuple[Tuple[int, ...], Tuple[int, ...]]] = set()

    while len(stacks[1]) != 0 and len(stacks[2]) != 0:
        begin_state = (tuple(stacks[1]), tuple(stacks[2]))
        if begin_state in seen_stacks:
            return 1  # game instantly ends in a win for player 1
        if winner(stacks[1], stacks[2]) == 1:
            stacks[1] = stacks[1][1:] + [stacks[1][0], stacks[2][0]]
            stacks[2] = stacks[2][1:]
        else:
            stacks[2] = stacks[2][1:] + [stacks[2][0], stacks[1][0]]
            stacks[1] = stacks[1][1:]
        seen_stacks.add(begin_state)

    return 1 if len(stacks[2]) == 0 else 2


def winner(stack_1: List[int], stack_2: List[int]) -> int:
    if stack_1[0] > len(stack_1) - 1 or stack_2[0] > len(stack_2) - 1:
        return 1 if stack_1[0] > stack_2[0] else 2
    else:
        return play_game(
            {1: stack_1[1 : stack_1[0] + 1], 2: stack_2[1 : stack_2[0] + 1]}
        )


def score(stack: List[int]) -> int:
    return sum((len(stack) - i) * card for i, card in enumerate(stack))


if __name__ == "__main__":
    main()
