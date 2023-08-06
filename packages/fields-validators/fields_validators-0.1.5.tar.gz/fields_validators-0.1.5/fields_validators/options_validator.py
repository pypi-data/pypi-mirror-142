from typing import Any

from .exceptions import InvalidFieldError

from .base_validator import BaseValidator


class OptionsValidator(BaseValidator):

    def __init__(self, field_name: str, *options) -> None:
        self._types = str
        self._field_name = field_name
        self._options = options

    def validate(self, data: Any) -> Any:
        if data in self._options:
            return data
        raise InvalidFieldError(
            self._field_name,
            f"Invalid option {data}. Available options are {self._options}"
        )
