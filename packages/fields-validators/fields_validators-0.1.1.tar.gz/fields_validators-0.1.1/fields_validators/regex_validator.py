import re
from typing import Any

from .exceptions import InvalidFieldError

from .base_validator import BaseValidator
from .type_validator import TypeValidator


class RegexValidator(BaseValidator):

    def __init__(self, field_name: str, regex: str) -> None:
        self._types = str
        self._field_name = field_name
        self._regex = regex
        self._type_validator = TypeValidator(field_name, str)

    def validate(self, data: Any) -> Any:
        self._type_validator.validate(data)

        if not re.search(self._regex, data):
            raise InvalidFieldError(
                self._field_name,
                f"the field: {self._field_name} don't match required regex"
            )
        return data
