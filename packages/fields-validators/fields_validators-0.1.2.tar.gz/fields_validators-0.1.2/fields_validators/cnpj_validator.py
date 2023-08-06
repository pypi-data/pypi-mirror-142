import re
from itertools import cycle
from typing import Any

from .exceptions import InvalidFieldError

from .base_validator import BaseValidator


class CNPJValidator(BaseValidator):

    def __get__(self, obj, obj_type):
        return obj._cnpj

    def __set__(self, obj, value):
        obj._cnpj = self.validate(value)

    def validate(self, data: Any) -> Any:
        cnpj = "".join([n for n in data if re.match(r"[0-9]", n)])

        LENGTH_CNPJ = 14
        if len(cnpj) != LENGTH_CNPJ:
            raise InvalidFieldError("CNPJ", detail="Invalid CNPJ")

        if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
            raise InvalidFieldError("CNPJ", detail="Invalid CNPJ")

        reversed_cnpj = cnpj[::-1]
        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), reversed_cnpj[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11

            if reversed_cnpj[i - 1:i] != str(dv % 10):
                raise InvalidFieldError("CNPJ", detail="Invalid CNPJ")
        return cnpj
