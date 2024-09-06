from dataclasses import dataclass

from core.base_types.type_checks import (
    assert_string_is_trimmed,
    assert_string_is_not_empty_or_none,
    assert_string_does_not_contain,
)


@dataclass(frozen=True)
class Code:
    value: str

    def __post_init__(self) -> None:
        assert_string_is_trimmed(self.value)
        assert_string_is_not_empty_or_none(self.value)
        assert_string_does_not_contain(self.value, " ")
