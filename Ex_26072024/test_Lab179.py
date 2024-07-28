# Fixture - Concept in python
# You can use the fixture
# context to the test.
# Similar - Pre condition,Post condition.

# Pre Condition - token, booking_id - Fixture
# test_Update_negative 1
# test_Update_positive 2

# setUp and TearDown- Pre- and Post-condition.

import pytest


@pytest.fixture()
def is_married():
    return True


def test_i_need_confirm(is_married):
    assert is_married == True
