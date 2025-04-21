import pytest
from app.queries import handle_user_query

def test_average_first_innings():
    result = handle_user_query("What’s the average first innings score at Wankhede?")
    assert "average first innings score" in result

def test_average_second_innings():
    result = handle_user_query("What’s the average second innings score at Chepauk?")
    assert "average second innings score" in result
