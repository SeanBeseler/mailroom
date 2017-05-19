"""Tests for mail.py."""


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


@pytest.mark.parametrize('amount, result', TEST_CHECK_AMOUNT_OUTPUT)
def test_check_amount(amount, result):
    """."""
    from mail import check_amount
    assert check_amount(amount) == result


@pytest.mark.parametrize('name, amount, result', THANK_YOU_PARAMS)
def test_print_thank_you(name, amount, result):
    """."""
    from mail import print_thank_you
    assert print_thank_you(name, amount) == result


def test_build_words():
    from mail import add_dic
    dic = {}
    name = 'sean'
    rdic{'sean':[0.00,0,0.00]}
    assert add_dic(dic, name) == rdic


def print_name_test():
    from mail import print_name
    rdic{'sean':[0.00,0,0.00]}
    assert print_name(rdic) == 'sean'


