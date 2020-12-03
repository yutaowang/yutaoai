from . import yutaoai

def test_yutaoai():
    assert yutaoai.apply("Jane") == "hello Jane"
