import pytest
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    # testing simple addition
    """
    assert 1 + 1 == 2
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    # testing that converting string to uppercase works
    """
    assert "hello".upper()  == "HELLO"
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    # testing whether sorting a list returns the correct order
    """
    data = [7, 6, 5, 4]
    data.sort()
    assert data == [4, 5, 6, 7]
    pass
