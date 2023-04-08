class FMError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message.split(" - ", 1)[1]
        super().__init__(self.message)


class Error(FMError):
    pass


class InvalidServiceError(FMError):
    pass


class InvalidMethodError(FMError):
    pass


class AuthenticationFailedError(FMError):
    pass


class InvalidFormatError(FMError):
    pass


class InvalidParametersError(FMError):
    pass


class InvalidResourceError(FMError):
    pass


class OperationFailedError(FMError):
    pass


class InvalidSessionKeyError(FMError):
    pass


class InvalidAPIKeyError(FMError):
    pass


class ServiceOfflineError(FMError):
    pass


class SubscribersOnlyError(FMError):
    pass


class InvalidMethodSignatureError(FMError):
    pass


class UnauthorizedTokenError(FMError):
    pass


class ItemNotAvailableError(FMError):
    pass


class ServiceUnavailableError(FMError):
    pass


class LoginError(FMError):
    pass


class TrialExpiredError(FMError):
    pass


class NotExistError(FMError):
    pass


class NotEnoughContentError(FMError):
    pass


class NotEnoughMembersError(FMError):
    pass


class NotEnoughFansError(FMError):
    pass


class NotEnoughNeighboursError(FMError):
    pass


class NoPeakRadioError(FMError):
    pass


class RadioNotFoundError(FMError):
    pass


class APIKeySuspendedError(FMError):
    pass


class DeprecatedError(FMError):
    pass


def get_error(code: int):
    ERRORS = {
        1: Error,
        2: InvalidServiceError,
        3: InvalidMethodError,
        4: AuthenticationFailedError,
        5: InvalidFormatError,
        6: InvalidParametersError,
        7: InvalidResourceError,
        8: OperationFailedError,
        9: InvalidSessionKeyError,
        10: InvalidAPIKeyError,
        11: ServiceOfflineError,
        12: SubscribersOnlyError,
        13: InvalidMethodSignatureError,
        14: UnauthorizedTokenError,
        15: ItemNotAvailableError,
        16: ServiceUnavailableError,
        17: LoginError,
        18: TrialExpiredError,
        19: NotExistError,
        20: NotEnoughContentError,
        21: NotEnoughMembersError,
        22: NotEnoughFansError,
        23: NotEnoughNeighboursError,
        24: NoPeakRadioError,
        25: RadioNotFoundError,
        26: APIKeySuspendedError,
        27: DeprecatedError,
    }
    return ERRORS.get(code, FMError)
