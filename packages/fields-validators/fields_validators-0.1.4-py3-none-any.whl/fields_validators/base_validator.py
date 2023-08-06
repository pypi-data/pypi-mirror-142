from abc import ABC, abstractmethod
from typing import Any


class BaseValidator(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def __get__(self, obj, obj_type):
        return getattr(obj, f"_{self._field_name}")

    def __set__(self, obj, value):
        return setattr(obj, f"_{self._field_name}", self.validate(value))
