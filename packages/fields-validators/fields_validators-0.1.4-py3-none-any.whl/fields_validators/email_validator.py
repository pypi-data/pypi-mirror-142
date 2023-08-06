from typing import Any

from .exceptions import InvalidFieldError

from .base_validator import BaseValidator
from .regex_validator import RegexValidator


class EmailValidator(BaseValidator):

    def __init__(self, field_name: str) -> None:
        self._types = str
        self._field_name = field_name
        self._regex_validator = RegexValidator(
            field_name, r"^([\w.-]+)([\w]+)@([\w\-]+\.)+[\w-]{2,4}$"
        )

    def validate(self, data: Any) -> Any:
        try:
            self._regex_validator.validate(data)
        except InvalidFieldError:
            raise InvalidFieldError(self._field_name, "Invalid email address")
        return data
