

import hypothesis.strategies

@hypothesis.given(hypothesis.strategies.integers())
@hypothesis.settings(max_examples = 1000)
def test_encode_decode(t):
    if t == -4:
        assert False
    assert t == t
