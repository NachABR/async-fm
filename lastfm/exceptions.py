class Error(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


class LastFMError:
    ERRORS = {
        1: "Error",
        2: "InvalidServiceError",
        3: "InvalidMethodError",
        4: "AuthenticationFailedError",
        5: "InvalidFormatError",
        6: "InvalidParametersError",
        7: "InvalidResourceError",
        8: "OperationFailedError",
        9: "InvalidSessionKeyError",
        10: "InvalidAPIKeyError",
        11: "ServiceOfflineError",
        12: "SubscribersOnlyError",
        13: "InvalidMethodSignatureError",
        14: "UnauthorizedTokenError",
        15: "ItemNotAvailableError",
        16: "ServiceUnavailableError",
        17: "LoginError",
        18: "TrialExpiredError",
        19: "NotExistError",
        20: "NotEnoughContentError",
        21: "NotEnoughMembersError",
        22: "NotEnoughFansError",
        23: "NotEnoughNeighboursError",
        24: "NoPeakRadioError",
        25: "RadioNotFoundError",
        26: "APIKeySuspendedError",
        27: "DeprecatedError",
    }

    @classmethod
    def get_error_class(cls, code: int):
        error_name = cls.ERRORS.get(code, "LastFMError")
        return globals().get(error_name, Error)
