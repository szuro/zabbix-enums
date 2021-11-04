from enum import IntEnum


class PreprocessingErrorHandler(IntEnum):
    ERROR_MESSAGE = 0
    DISCARD_VALUE = 1
    CUSTOM_VALUE = 2
    CUSTOM_ERROR_MESSAGE = 3
