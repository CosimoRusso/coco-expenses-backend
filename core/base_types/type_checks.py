def assert_string_is_trimmed(string: str) -> None:
    assert string == string.strip(), f"String is not trimmed."


def assert_string_is_not_empty_or_none(string: str) -> None:
    assert string, f"String is empty."


def assert_string_does_not_contain(string: str, forbidden: str) -> None:
    assert (
        forbidden not in string
    ), f"String contains forbidden character '{forbidden}'."
