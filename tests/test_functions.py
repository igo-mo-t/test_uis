from project.functions import days_between_dates, remove_k_digits


def test_days_between_dates():
    """
    GIVEN days_between_dates function
    WHEN function call
    THEN correct return
    """
    assert days_between_dates("2019-06-29", "2019-06-30") == {
        "Number of days between dates": 1
    }
    assert days_between_dates("2020-01-15", "2019-12-14") == {
        "Number of days between dates": 31
    }


def test_remove_k_digits():
    """
    GIVEN days_between_dates function
    WHEN function call
    THEN correct return
    """
    assert remove_k_digits("1432219", 3) == {
        "The minimum number after removing 'k' digits from the string 'num'": "1219"
    }
    assert remove_k_digits("10200", 1) == {
        "The minimum number after removing 'k' digits from the string 'num'": "200"
    }
