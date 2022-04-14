import string
from truerandom.truerandom import (
    true_choice,
    true_password,
    true_passwords,
    true_randint,
    true_shuffle
)


def str_contains_one_of(string, char_list):
    for char in string:
        if char in char_list:
            return True
    return False


# RANDINT

def test_randint():
    assert true_randint(ge=0, le=1) in range(0, 1)


def test_randint_ge_lower_than_le():
    try:
        true_randint(ge=1, le=0)
        assert False
    except ValueError:
        assert True


def test_randint_ge_equals_le():
    assert true_randint(ge=42, le=42) == 42


def test_randint_ge_negative():
    assert true_randint(ge=-42, le=42) in range(-42, 42)


# CHOICE

def test_choice_with_tuple():
    CHOICES = (40, 50, 60, 70)
    assert true_choice(CHOICES) in CHOICES


def test_choice_with_list():
    CHOICES = [40, 50, 60, 70]
    assert true_choice(CHOICES) in CHOICES


def test_choice_with_generator():
    CHOICES = [40, 50, 60, 70]

    def choices():
        for nb in CHOICES:
            yield nb
    try:
        true_choice(choices())
        assert False
    except TypeError:
        assert True


# SHUFFLE

def test_shuffle():
    LIST = [40, 50, 60, 70]

    randomized_list = LIST.copy()

    true_shuffle(LIST)
    assert len(randomized_list) == len(LIST)
    assert sorted(LIST) == sorted(randomized_list)


# PASSWORD

def test_password_length():
    LENGTH = 10
    pswd = true_password(length=LENGTH)
    assert len(pswd) == LENGTH


def test_password_too_short():
    LENGTH = 7
    try:
        true_password(length=LENGTH)
        assert False
    except ValueError:
        pass


def test_password_content():

    pswd = true_password(
        has_punctuation=True,
        has_uppercase_letters=True,
        has_digits=True
    )

    assert str_contains_one_of(pswd, list(string.punctuation))
    assert str_contains_one_of(pswd, list(string.digits))
    assert str_contains_one_of(pswd, list(string.ascii_uppercase))
    assert str_contains_one_of(pswd, list(string.ascii_lowercase))


def test_password_content_with_punc_only():

    pswd = true_password(
        has_punctuation=True,
        has_uppercase_letters=False,
        has_digits=False
    )

    assert str_contains_one_of(pswd, list(string.punctuation))
    assert not str_contains_one_of(pswd, list(string.digits))
    assert not str_contains_one_of(pswd, list(string.ascii_uppercase))
    assert str_contains_one_of(pswd, list(string.ascii_lowercase))


def test_password_content_with_dig_only():

    pswd = true_password(
        has_punctuation=False,
        has_uppercase_letters=False,
        has_digits=True
    )

    assert not str_contains_one_of(pswd, list(string.punctuation))
    assert str_contains_one_of(pswd, list(string.digits))
    assert not str_contains_one_of(pswd, list(string.ascii_uppercase))
    assert str_contains_one_of(pswd, list(string.ascii_lowercase))


def test_password_content_with_upc_only():

    pswd = true_password(
        has_punctuation=False,
        has_uppercase_letters=True,
        has_digits=False
    )

    assert not str_contains_one_of(pswd, list(string.punctuation))
    assert not str_contains_one_of(pswd, list(string.digits))
    assert str_contains_one_of(pswd, list(string.ascii_uppercase))
    assert str_contains_one_of(pswd, list(string.ascii_lowercase))


# PASSWORDS

def test_passwords_nb():

    assert len(true_passwords(nb=10)) == 10


def test_passwords_length():

    assert len(true_passwords(nb=1, length=8)[0]) == 8


def test_passwords_too_short():

    LENGTH = 7
    try:
        true_passwords(nb=1, length=LENGTH)
        assert False
    except ValueError:
        pass


def test_passwords_nb_less_than_1():

    NB = 0
    try:
        true_passwords(nb=NB)
        assert False
    except ValueError:
        pass

    NB = -1
    try:
        true_passwords(nb=NB)
        assert False
    except ValueError:
        pass
