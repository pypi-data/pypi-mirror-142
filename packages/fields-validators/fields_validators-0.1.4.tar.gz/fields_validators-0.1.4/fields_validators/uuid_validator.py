from uuid import UUID

from .base_validator import BaseValidator
from .exceptions import InvalidFieldError


class UUIDValidator(BaseValidator):

    def __init__(self, version: int = 4) -> None:
        self._version = version

    def _validate(self, value: str) -> bool:
        try:
            UUID(value, version=self._version)
            return True
        except ValueError:
            return False

    def validate(self, value: str) -> str:
        if type(value) is not str or not self._validate(value):
            raise InvalidFieldError("id", f"is not a valid uuid{self._version}")

        return value
