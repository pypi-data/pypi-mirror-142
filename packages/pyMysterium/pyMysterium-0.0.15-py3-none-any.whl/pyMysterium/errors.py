class MystAPIError(Exception):
    """Default Mysterium API Error
Raised when unknown error has occured"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TopUpError(MystAPIError):
    """Raised when there's an error creating a topup order"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InternalServerError(MystAPIError):
    """Raised when myst tequila API experiences an **internal server error**"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BadRequestError(MystAPIError):
    """Raised when there's a non 200 response code from server"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ParameterValidationError(MystAPIError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
class RegistrationAlreadyInProgressError(MystAPIError):
    """Raised when registration is alredy in progress"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ServiceUnavailableError(MystAPIError):
    """Raised when a service isn't available"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class MinimumAmountError(TopUpError):
    """Raised when topup amount is less than minimum suggested amount"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class MinimumPassphraseLengthError(MystAPIError):
    """Raised when export password doesnt meet length requirements"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ExportError(MystAPIError):
    """Raised when there's an error exporting current identity"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)