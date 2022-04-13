from typing import List, Tuple
import string
from typing import Any
import quantumrandom as qtr

GENERATOR = qtr.cached_generator()


def true_randint(
    ge: int,
    le: int
) -> int:
    """
        Returns a random integer between <ge> and <le>
    """
    return int(qtr.randint(min=ge, max=le, generator=GENERATOR))


def true_choice(
    x: List | Tuple
) -> Any:
    """
        Returns a random item from the list <x>
    """
    return x[true_randint(0, len(x) - 1)]


def true_shuffle(
    x: List
) -> None:
    """
        Shuffle list <x> in place, and return None.
    """
    for i in reversed(range(1, len(x))):
        j = true_randint(0, i + 1)
        x[i], x[j] = x[j], x[i]


def true_password(
    length: int = 10,
    has_punctuation: bool = True,
    has_uppercase_letters: bool = True,
    has_digits: bool = True
) -> str:
    """
        Generates a true random password composed of
        <length> character(s) composed of eventually:
        - punctuations
        - uppercase letters
        - digits
        - lowercase letters
    """

    if length < 8:
        raise Exception(
            "Password length must be greater or equal than 8 characters")

    password = ""

    max_part_length = (length - 1) // (
        int(has_punctuation) + int(has_uppercase_letters) + int(has_digits))

    if has_punctuation:
        for _ in range(true_randint(1, max_part_length)):
            password += true_choice(string.punctuation)
            length -= 1

    if has_uppercase_letters:
        for _ in range(true_randint(1, max_part_length)):
            password += true_choice(string.ascii_uppercase)
            length -= 1

    if has_digits:
        for _ in range(true_randint(1, max_part_length)):
            password += true_choice(string.digits)
            length -= 1

    for _ in range(length):
        password += true_choice(string.ascii_lowercase)

    password = list(password)
    true_shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print(true_password(length=12))
