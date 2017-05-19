"""Tests for mail.py."""


import pytest


TEST_CHECK_AMOUNT_OUTPUT = [
    ('100', 100.0),
    ('10.01', 10.01),
    ('He was', False),
    ('1,000.10', 1000.10)
]


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
