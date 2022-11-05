from commitparser.parse_commit import parse_commit


def test_commit_message():
    assert parse_commit('submit ~UB Hacking Submission~ parse_commit.py') == ('UB Hacking Submission', 'parse_commit.py')


def test_add_one_z():
    try:
        parse_commit(1)
        assert False
    except AttributeError:
        assert True
