from hello import add


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    from hello import add
    assert add(-1, 1) == 0
