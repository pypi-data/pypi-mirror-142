from ..fmt import Color, TextConfig

TEXT_DEBUG_CONFIG = TextConfig(Color.GRAY)
TEXT_INFO_CONFIG = TextConfig(Color.WHITE)
TEXT_WARNING_CONFIG = TextConfig(Color.YELLOW)
TEXT_ERROR_CONFIG = TextConfig(Color.DARK_RED)
TEXT_CRITICAL_CONFIG = TextConfig(Color.DARK_RED)

EXCEPTION_INFORMATION = {
    NotImplementedError: "this feature is not implemented",
}
