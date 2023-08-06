from .base import BaseError


class MissingFieldError(BaseError):

    def __init__(self, field_name: str, detail: str = "") -> None:
        super().__init__(
            detail=detail,
            error_info=f"Missing field: {field_name}",
        )


class InvalidFieldError(BaseError):

    def __init__(self, field_name: str, detail: str = "") -> None:
        super().__init__(
            detail=detail,
            error_info=f"Invalid field value: {field_name}",
        )


class InvalidTypeError(BaseError):

    def __init__(
            self,
            field_name: str,
            expected_type: str,
            received_type: str,
    ) -> None:
        super().__init__(
            detail=f"Expected {expected_type} received {received_type}",
            error_info=f"Invalid type to the field: {field_name}",
        )
