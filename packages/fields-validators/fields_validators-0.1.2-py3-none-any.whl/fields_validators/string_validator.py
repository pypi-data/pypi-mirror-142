from typing import Any

from .exceptions import InvalidFieldError

from .base_validator import BaseValidator
from .type_validator import TypeValidator


class StrValidator(BaseValidator):

    def __init__(self, field_name: str, min_len: int, max_len: int) -> None:
        self._types = str
        self._field_name = field_name
        self._min_len = min_len
        self._max_len = max_len
        self._type_validator = TypeValidator(field_name, str)

    def validate(self, data: Any) -> Any:
        self._type_validator.validate(data)

        if self._min_len > 0 and len(data) < self._min_len:
            raise InvalidFieldError(
                self._field_name, f"the length should be > {self._min_len}"
            )

        if 0 < self._max_len < len(data):
            raise InvalidFieldError(
                self._field_name, f"the length should be < {self._max_len}"
            )
        return data
