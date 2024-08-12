from lib.admin import *
import pytest

"""
Test the date given is in the right format
"""
def test_right_format():
    with pytest.raises(Exception) as e:
        give_access("09-11-1998")
    error_message = str(e.value)
    assert error_message == "String is not in the correct format"
"""
Test that the date given is valid e.g. not after today
"""
def test_date_in_range():
    assert give_access("2050-10-09") == "User can't be born after today"

"""
Test that a user over 16 is granted access
"""
def test_user_over_16():
    assert give_access("1990-10-09") == "Access has been granted"


"""
Test that a user under 16 is denied access
"""

def test_user_under_16():
    assert give_access("2010-10-09") == "Access has been denied. You are 13 years old and you need to be at least 16 years old for access."