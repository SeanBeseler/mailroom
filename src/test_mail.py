"""Tests for mial.py."""


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

def add_dic_test():
    """."""
    from mial import add_dic
    dic ={}
    name = 'sean'
    rdic{'sean':[0.00,0,0.00]}
        assert add_dic(dic, name) == rdic

def print_name_test():
    """."""
    from mial import print_name
    rdic{'sean':[0.00,0,0.00]}
        assert print_name(rdic) == 'sean'


