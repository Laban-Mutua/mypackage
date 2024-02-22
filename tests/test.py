from mypackage import mymodule

def test_top_n():
    """
    Make sure top_n works correctly
    """

    assert mymodule.top_n([8,3,2,7,4], 3) == [8,7,4], "incorrect"
    assert mymodule.top_n([10,38,3,7], 2) == [38,10], "incorrect"
    assert mymodule.top_n([12,3,0,2,7,9], 4) == [12,9,7,3], "incorrect"