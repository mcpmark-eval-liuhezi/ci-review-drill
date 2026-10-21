from app import greet


def test_greet_includes_name():
    assert "world" in greet("world")


def test_greet_is_friendly():
    result = greet("Ada")
    assert "Hello" in result
    assert "!" in result
    assert "welcome" in result.lower()
