try:
    from mlpractice_solutions.mlpractice_solutions\
        .rnn_torch_solution import make_token_to_id
except ImportError:
    make_token_to_id = None


def test_all(make_token_to_id=make_token_to_id):
    test_len(make_token_to_id)
    test_simple(make_token_to_id)
    print('All tests passed!')


def test_len(make_token_to_id=make_token_to_id):
    tokens = ["Make", "ML", "great"]

    assert len(make_token_to_id(tokens)) == len(tokens), \
        "Dictionaries must have same size as tokens list"


def test_simple(make_token_to_id=make_token_to_id):
    tokens = ["Make", "ML", "great"]
    expected = {token : id_ for id_, token in enumerate(tokens)}

    assert make_token_to_id(tokens) == expected, \
        "Have you heard of the dict datatype in Python?"
