from collections import deque
from typing import Set, Tuple


def read_data(path: str) -> (deque, deque):
    with open(path) as f:
        lines = f.read()

    lines = lines.split("\n")

    cards1, cards2 = deque(), deque()

    for line in lines:
        if line == "":
            continue
        elif line == "Player 1:":
            cards = cards1
        elif line == "Player 2:":
            cards = cards2
        else:
            cards.append(int(line))

    return cards1, cards2


def play_1(cards1: deque, cards2: deque) -> deque:
    while cards1 and cards2:
        top1, top2 = cards1.popleft(), cards2.popleft()
        if top1 > top2:
            cards1.append(top1)
            cards1.append(top2)
        else:
            cards2.append(top2)
            cards2.append(top1)

    return cards1 or cards2


game = 1


def play_2(cards1: deque, cards2: deque) -> int:
    global game
    _round = 0
    previous: Set[Tuple[Tuple[int]]] = set()
    # print()
    # print(f"=== Game {game} ===")

    while cards1 and cards2:
        # Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
        if (all_cards := (tuple(cards1), tuple(cards2))) in previous:
            winner = 1
            break

        previous.add(all_cards)

        _round += 1
        # print()
        # print(f"-- Round {_round} (Game {game}) --")
        # print("Player 1's deck:", ", ".join(str(x) for x in cards1))
        # print("Player 2's deck:", ", ".join(str(x) for x in cards2))

        # Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
        top1, top2 = cards1.popleft(), cards2.popleft()
        # print("Player 1 plays:", top1)
        # print("Player 2 plays:", top2)

        # If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
        if top1 <= len(cards1) and top2 <= len(cards2):
            # To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the 3 card, their deck in the sub-game would be copies of the next three cards in their deck.)
            # print("Playing a sub-game to determine the winner...")
            game += 1
            winner, _ = play_2(deque(list(cards1)[:top1]),
                               deque(list(cards2)[:top2]))
            game -= 1

        # Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.

        elif top1 > top2:
            winner = 1
        else:
            winner = 2

        # print(f"Player {winner} wins round {_round} of game {game}!")

        if winner == 1:
            cards1.append(top1)
            cards1.append(top2)
        else:
            cards2.append(top2)
            cards2.append(top1)

    # print(f"The winner of game {game} is player {winner}!")
    return winner, cards1 or cards2


def calculate_score(winner: deque) -> int:
    total = 0

    for x in zip(winner, range(len(winner), 0, -1)):
        total += x[0] * x[1]

    return total


cards1, cards2 = read_data("22/input.txt")

win_cards = play_1(cards1, cards2)

print(calculate_score(win_cards))

cards1, cards2 = read_data("22/input.txt")

winner, win_cards = play_2(cards1, cards2)

print(calculate_score(win_cards))
