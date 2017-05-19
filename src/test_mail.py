"""Tests for mial.py."""


import pytest


TEST_CHECK_AMOUNT_OUTPUT = [
    ('100', 100.0),
    ('10.01', 10.01),
    ('He was', False),
    ('1,000.10', 1000.10)
]

test_dict = {
    '1888--I was': ['returning'],
    'new problem.': ['I'],
    'see Holmes': ['again,'],
    'the blind.': ['He'],
    'had now': ['returned'],
    'his drug-created': ['dreams']
}


@pytest.mark.parametrize('amount, result', TEST_CHECK_AMOUNT_OUTPUT)
def test_check_amount(amount, result):
    """."""
    from mail import check_amount
    assert check_amount(amount) == result

'''
def test_get_random():
    """."""
    from trigrams import get_random
    for n in range(1, 100):
        assert get_random(n) in range(n)


def test_build_words():
    """."""
    from trigrams import build_words
    for n in range(10, 100):
        assert len(build_words(n, test_dict).split()) == n
    '''
