from typing import List, Tuple
import string
import csv
from typing import Any

import quantumrandom as qtr

GENERATOR = qtr.cached_generator()
CSV_QUOTE_SEPARATOR = "|"


def true_randint(
    ge: int,
    le: int
) -> int:
    """
        Returns a random integer between <ge> and <le>
    """
    if not isinstance(ge, int) or not isinstance(le, int):
        raise TypeError("ge and le must be integers")

    return int(qtr.randint(min=ge, max=le, generator=GENERATOR))


def true_choice(
    x: List | Tuple
) -> Any:
    """
        Returns a random item from the list <x>
    """
    if not isinstance(x, List) and not isinstance(x, Tuple) \
            and not isinstance(x, str):
        raise TypeError(f"x must be a list or a tuple (instead of {type(x)})")

    return x[true_randint(0, len(x) - 1)]


def true_shuffle(
    x: List
) -> None:
    """
        Shuffles list <x> in place, and returns None.
    """
    if not isinstance(x, List):
        raise TypeError(f"x must be a list (instead of {type(x)})")

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
        Generates a random password composed of <length> character(s) with:
        - 0 or more punctuations
        - 0 or more uppercase letters
        - 0 or more digits
        - Remaining slots are filled with lowercase letters.
    """

    if not isinstance(length, int):
        raise TypeError("param 'length' must be an integer")

    if not isinstance(has_punctuation, bool):
        raise TypeError("param 'has_punctuation' must be a boolean")

    if not isinstance(has_uppercase_letters, bool):
        raise TypeError("param 'has_uppercase_letters' must be a boolean")

    if not isinstance(has_digits, bool):
        raise TypeError("param 'has_digits_letters' must be a boolean")

    if length < 8:
        raise ValueError(
            "param 'length' must be >= 8")

    password = ""

    max_part_length = (length - 1) // (
        int(has_punctuation) + int(has_uppercase_letters) + int(has_digits))

    punctuation = [
        punc for punc in string.punctuation if punc != CSV_QUOTE_SEPARATOR]

    if has_punctuation:
        for _ in range(true_randint(1, max_part_length)):
            password += true_choice(punctuation)
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


def true_passwords(
    nb: int,
    csv_output: str = None,
    length: int = 10,
    has_punctuation: bool = True,
    has_uppercase_letters: bool = True,
    has_digits: bool = True,
) -> List[str] | None:
    """
        Generate a csv file containing <nb> true passwords
    """
    if not isinstance(nb, int):
        raise TypeError("param 'nb' must be an integer")

    if csv_output:
        if not isinstance(nb, str):
            raise TypeError("param 'csv_output' must be a str")

    if not isinstance(length, int):
        raise TypeError("param 'length' must be an integer")

    if not isinstance(has_punctuation, bool):
        raise TypeError("param 'has_punctuation' must be a boolean")

    if not isinstance(has_uppercase_letters, bool):
        raise TypeError("param 'has_uppercase_letters' must be a boolean")

    if not isinstance(has_digits, bool):
        raise TypeError("param 'has_digits_letters' must be a boolean")

    if nb <= 0:
        raise Exception("param 'nb' must be stricly positive")

    if length < 8:
        raise ValueError(
            "param 'length' must be >= 8")

    if csv_output is not None:
        with open(csv_output, 'w', newline='', encoding='utf8') as csvfile:
            writer = csv.writer(
                csvfile,
                delimiter=' ',
                quotechar='|',
                quoting=csv.QUOTE_MINIMAL
            )
            for _ in range(nb):
                writer.writerow(
                    [
                        true_password(
                            length, has_punctuation,
                            has_uppercase_letters, has_digits
                        )])
    else:
        return [
            true_password(
                length, has_punctuation,
                has_uppercase_letters, has_digits
            ) for _ in range(nb)]
