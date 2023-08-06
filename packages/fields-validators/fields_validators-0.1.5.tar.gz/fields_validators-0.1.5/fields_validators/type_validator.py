from typing import Any

from .exceptions import InvalidTypeError

from .base_validator import BaseValidator


class TypeValidator(BaseValidator):

    def __init__(self, field_name: str, *allowed_types) -> None:
        self._types = allowed_types
        self._field_name = field_name

    def validate(self, data: Any) -> Any:
        received_type = type(data)
        if type(data) not in self._types:
            raise InvalidTypeError(
                field_name=self._field_name,
                expected_type=str([t.__name__ for t in self._types]),
                received_type=received_type.__name__
            )
        return data
