from prac import add


def test_add() -> None:
    result = add(2, 3)
    assert result == 5
