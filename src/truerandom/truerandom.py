from typing import List, Tuple
import string
from typing import Any
import quantumrandom as qtr


def true_randint(
    ge: int,
    le: int
) -> int:
    """
        Returns a random integer between <ge> and <le>
    """
    return int(qtr.randint(ge, le))


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
    min_nb_of_pct_characters: int = 1,
    min_nb_of_upc_letters: int = 1,
    min_nb_of_digits: int = 1
) -> str:
    """
        Generates a trully random password composed of
        <length> character including at least:
        - <min_nb_of_pct_characters punctionation> characters
        - <min_nb_of_upc_letters> characters
        - <min_nb_of_digits> characters
    """

    password = ""

    assert min_nb_of_pct_characters + min_nb_of_upc_letters \
        + min_nb_of_digits < length - 1
    max_part_length = (length - 1) // 3

    for _ in range(
            int(true_randint(min_nb_of_pct_characters, max_part_length))):
        password += true_choice(string.punctuation)
        length -= 1

    for _ in range(
            int(true_randint(min_nb_of_upc_letters, max_part_length))):
        password += true_choice(string.ascii_uppercase)
        length -= 1

    for _ in range(
            int(true_randint(min_nb_of_digits, max_part_length))):
        password += true_choice(string.digits)
        length -= 1

    for _ in range(length):
        password += true_choice(string.ascii_lowercase)

    password = list(password)
    true_shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print(true_password())
