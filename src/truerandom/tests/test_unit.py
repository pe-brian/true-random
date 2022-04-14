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


def test_true_randint():
    assert true_randint(ge=0, le=1) in range(0, 1)


def test_true_randint_ge_lower_than_le():
    try:
        true_randint(ge=1, le=0)
        assert False
    except ValueError:
        assert True


def test_true_randint_ge_equals_le():
    assert true_randint(ge=42, le=42) == 42


def test_true_randint_ge_negative():
    assert true_randint(ge=-42, le=42) in range(-42, 42)


def test_true_randint_wrong_input_types():
    try:
        true_randint(ge="narine", le=42)
        return False
    except TypeError:
        return True


def test_true_choice_with_tuple():
    CHOICES = (40, 50, 60, 70)
    assert true_choice(CHOICES) in CHOICES


def test_true_choice_with_list():
    CHOICES = [40, 50, 60, 70]
    assert true_choice(CHOICES) in CHOICES


def test_true_choice_with_generator():
    CHOICES = [40, 50, 60, 70]

    def choices():
        for nb in CHOICES:
            yield nb
    try:
        true_choice(choices())
        assert False
    except TypeError:
        assert True


def test_true_shuffle():
    LIST = [40, 50, 60, 70]

    randomized_list = LIST.copy()

    true_shuffle(LIST)
    assert len(randomized_list) == len(LIST)
    assert sorted(LIST) == sorted(randomized_list)


def test_true_shuffle_param_wrong_type():
    TUPLE = (40, 50, 60, 70)

    try:
        true_shuffle(TUPLE)
        return False
    except TypeError:
        return True


def test_true_password_length():
    LENGTH = 10
    pswd = true_password(length=LENGTH)
    assert len(pswd) == LENGTH


def test_true_password_content():

    pswd = true_password(
        has_punctuation=True,
        has_uppercase_letters=True,
        has_digits=True
    )

    assert str_contains_one_of(pswd, list(string.punctuation))
    assert str_contains_one_of(pswd, list(string.digits))
    assert str_contains_one_of(pswd, list(string.ascii_uppercase))
    assert str_contains_one_of(pswd, list(string.ascii_lowercase))


def test_true_password_content_with_punc_only():

    pswd = true_password(
        has_punctuation=True,
        has_uppercase_letters=False,
        has_digits=False
    )

    assert str_contains_one_of(pswd, list(string.punctuation))
    assert not str_contains_one_of(pswd, list(string.digits))
    assert not str_contains_one_of(pswd, list(string.ascii_uppercase))
    assert str_contains_one_of(pswd, list(string.ascii_lowercase))


def test_true_password_content_with_dig_only():

    pswd = true_password(
        has_punctuation=False,
        has_uppercase_letters=False,
        has_digits=True
    )

    assert not str_contains_one_of(pswd, list(string.punctuation))
    assert str_contains_one_of(pswd, list(string.digits))
    assert not str_contains_one_of(pswd, list(string.ascii_uppercase))
    assert str_contains_one_of(pswd, list(string.ascii_lowercase))


def test_true_password_content_with_upc_only():

    pswd = true_password(
        has_punctuation=False,
        has_uppercase_letters=True,
        has_digits=False
    )

    assert not str_contains_one_of(pswd, list(string.punctuation))
    assert not str_contains_one_of(pswd, list(string.digits))
    assert str_contains_one_of(pswd, list(string.ascii_uppercase))
    assert str_contains_one_of(pswd, list(string.ascii_lowercase))


def test_true_password_too_short():

    try:
        true_password(length=7)
        assert False
    except ValueError:
        assert True


def test_true_passwords():

    assert len(true_passwords(nb=10)) == 10
