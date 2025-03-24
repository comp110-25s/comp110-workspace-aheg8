"""Exercise 2 of Comp110 constructing Wordle!"""

__author__ = "730821126"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    idx = 0
    max_idx = 6
    won = False

    while idx < max_idx and not won:
        print(f"=== Turn {idx + 1}/{max_idx} ===")
        guess = input_guess(len(secret))
        result = emojified(secret, guess)
        print(result)

        if guess == secret:
            won = True
            print(f"You won in {idx + 1}/6 turns!")
        idx += 1
    if not won:
        print("X/6 - Sorry, try again tomrrow!")


def contains_char(guess_string: str, single_character: str) -> bool:
    """Checks if our single character is found in the guess."""
    assert len(single_character) == 1, f"len('{single_character}') is not 1"

    idx: int = 0
    while idx < len(guess_string):
        if guess_string[idx] == single_character:
            return True
        else:
            idx = idx + 1

    return False


def emojified(guess_emoji: str, secret_emoji: str) -> str:
    """Returns a string of emojis which represents the accuracy of the guess."""
    assert len(guess_emoji) == len(secret_emoji), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    idx: int = 0
    result: str = ""

    while idx < len(guess_emoji):
        if guess_emoji[idx] == secret_emoji[idx]:
            result = result + GREEN_BOX
        elif contains_char(secret_emoji, guess_emoji[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

        idx = idx + 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess and continue prompting
    them until they provide a guess of the expected length."""

    guess = input(f"Enter a {expected_length} character word.")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess
