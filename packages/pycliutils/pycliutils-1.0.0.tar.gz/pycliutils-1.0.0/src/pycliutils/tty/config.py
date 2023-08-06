from ..fmt import Color, TextConfig, TextFormat

QUESTION_FORMAT = TextConfig(color=Color.PURPLE)

CURSOR_DEFAULT_FORMAT = TextConfig(color=Color.NONE, color_bg=Color.NONE, attrs=[TextFormat.DARK])
CURSOR_ERROR_FORMAT   = TextConfig(color=Color.RED, color_bg=Color.NONE, attrs=[TextFormat.DARK])

CURSOR_ERROR_TIME = 0.6

AUTO_INLINE_MAX_CHARACTER_COUNT = 30

QUESTION_PREFIX = ">>> "
QUESTION_INLINE_SUFFIX = ": "
