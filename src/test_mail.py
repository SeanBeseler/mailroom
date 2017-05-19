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


UPDATE_PARAMS = [
    ({'James': [300.0, 1, 300.0], 'Sean': [100.0, 1, 100.0]}, 'James', 100.0, {'James': [400.0, 2, 200.0], 'Sean': [100.0, 1, 100.0]}),
    ({'James': [300.0, 1, 300.0], 'Sean': [100.0, 1, 100.0]}, 'Sean', 2000.0, {'James': [300.0, 1, 300.0], 'Sean': [2100.0, 2, 1050.0]})
]

CAT_NAME_PARAMS = [
    ('James', 'James             '),
    ('This name is way too long', 'This name is way t'),
    ('Okay length', 'Okay length       '),
    ('3', '3                 ')
]

CAT_NUM_PARAMS = [
    ('13', '13   '),
    (13, '13   '),
    ('25890012', '25890'),
    (1213421, '12134')
]

CAT_DON_PARAMS = [
    ('26', '26           '),
    (13, '13           '),
    ('25890012', '25890012     '),
    (1213421, '1213421      '),
    ('123456789012345', '1234567890123')
]


@pytest.mark.parametrize('dictionary, name, float, result', UPDATE_PARAMS)
def test_update_dic(dictionary, name, float, result):
    """Test to see if we get the updated dictionary back."""
    from mail import update_dic
    assert update_dic(dictionary, name, float) == result


@pytest.mark.parametrize('input, result', CAT_NAME_PARAMS)
def test_cat_name_space(input, result):
    """Test to see if the right number of spaces are being added."""
    from mail import cat_name_space
    assert cat_name_space(input) == result


@pytest.mark.parametrize('input, result', CAT_NUM_PARAMS)
def test_cat_num_space(input, result):
    """Test to see if the right number of spaces are being added."""
    from mail import cat_num_space
    assert cat_num_space(input) == result


@pytest.mark.parametrize('input, result', CAT_DON_PARAMS)
def test_cat_donation_space(input, result):
    """Test to see if the right number of spaces are being added."""
    from mail import cat_donation_space
    assert cat_donation_space(input) == result


def test_add_dic():
    from mail import add_dic
    dic = {}
    name = 'sean'
    rdic = {'sean': [0.00, 0, 0.00]}
    assert add_dic(dic, name) == rdic


def print_name_test():
    from mail import print_name
    rdic = {'sean': [0.00, 0, 0.00]}
    assert print_name(rdic) == 'sean'
