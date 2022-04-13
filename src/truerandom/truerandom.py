from typing import List, Tuple
import string
import csv
from typing import Any

import quantumrandom as qtr

GENERATOR = qtr.cached_generator()
CSV_SEPARATOR = "|"


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
        Shuffles list <x> in place, and returns None.
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
            "Length must be greater or equal than 8 characters")

    password = ""

    max_part_length = (length - 1) // (
        int(has_punctuation) + int(has_uppercase_letters) + int(has_digits))

    punctuation = [
        punc for punc in string.punctuation if punc != CSV_SEPARATOR]

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
    csv_output: str,
    length: int = 10,
    has_punctuation: bool = True,
    has_uppercase_letters: bool = True,
    has_digits: bool = True,
) -> None:
    """
        Generate a csv file containing <nb> true passwords
    """
    if nb <= 0:
        raise Exception("nb param must be positive")

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


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='Create a csv file containing generated passwords.')
    parser.add_argument('--nb', type=int, default=100,
                        help='number of passwords to generate')
    parser.add_argument('--length', type=int, default=12,
                        help='length of passwords')
    parser.add_argument('--csv', type=str, required=True,
                        help='CSV filepath where to write passwords')
    parser.add_argument('--punctuation', type=bool, default=True,
                        help='Password has punctuation')
    parser.add_argument('--digits', type=bool, default=True,
                        help='Password has digits')
    parser.add_argument('--uppercase', type=bool, default=True,
                        help='Password has uppercase letters')

    args = parser.parse_args()
    true_passwords(
        nb=args.nb,
        csv_output=args.csv,
        length=args.length,
        has_punctuation=args.punctuation,
        has_uppercase_letters=args.uppercase,
        has_digits=args.digits
    )
