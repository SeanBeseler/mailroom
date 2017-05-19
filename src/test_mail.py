"""Tests for mial.py."""


import pytest


TEST_CHECK_AMOUNT_OUTPUT = [
    ('100', 100.0),
    ('10.01', 10.01),
    ('He was', False),
    ('1,000.10', 1000.10)
]

THANK_YOU_PARAMS = [
    ('bob', 100.0, 'Thank you for donation of $100.00. South Carolina \
Association of Magicians appreciate your support!\n\nSincerely,\nCode Dudes'),
    ('will', 1500.42, 'Thank you for donation of $1500.42. South Carolina \
Association of Magicians appreciate your support!\n\nSincerely,\nCode Dudes'),
    ('Tommy Wayne', 10.0, 'Thank you for donation of $10.00. South Carolina \
Association of Magicians appreciate your support!\n\nSincerely,\nCode Dudes'),
    ('John John', 3456.71, 'Thank you for donation of $3456.71. South Carolina \
Association of Magicians appreciate your support!\n\nSincerely,\nCode Dudes')
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
'''

@pytest.mark.parametrize('name, amount, result', THANK_YOU_PARAMS)
def test_print_thank_you(name, amount, result):
    """."""
    from mail import print_thank_you
    assert print_thank_you(name, amount) == result

'''
def test_build_words():
    """."""
    from trigrams import build_words
    for n in range(10, 100):
        assert len(build_words(n, test_dict).split()) == n
    '''
