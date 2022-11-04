from simplepythonpackage.add_one import add_one


def test_add_one_1():
    assert add_one(1) == 2


def test_add_one_z():
    try:
        add_one('z')
        assert False
    except TypeError:
        assert True
