import sys




class BaseError(Exception):

    def __init__(
        self,
        detail: str,
        error_info: str,
    ) -> None:
        self.traceback = sys.exc_info()
        self.detail = detail
        self.error_info = error_info
        super().__init__(error_info)
