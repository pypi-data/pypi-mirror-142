from typing import Any

from .exceptions import InvalidFieldError

from .base_validator import BaseValidator


class CPFValidator(BaseValidator):

    def __get__(self, obj, obj_type):
        return obj._cpf

    def __set__(self, obj, value):
        obj._cpf = self.validate(value)

    def validate(self, data: Any) -> Any:
        cpf = [char for char in data if char.isdigit()]

        if len(cpf) != 11:
            raise InvalidFieldError("CPF")

        if cpf == cpf[::-1]:
            raise InvalidFieldError("CPF")

        for i in range(9, 11):
            value = sum(
                (int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
            )
            digit = int(((value * 10) % 11) % 10)
            if digit != int(cpf[i]):
                raise InvalidFieldError("CPF", detail="Invalid CPF")
        return "".join(cpf)
