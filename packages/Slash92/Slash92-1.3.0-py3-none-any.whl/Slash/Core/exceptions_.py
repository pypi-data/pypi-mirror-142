class SlashTypeError(Exception):
    def __init__(self, text) -> None: ...


class SlashRulesError(Exception):
    def __init__(self, text) -> None: ...


class SlashBadColumnNameError(Exception):
    def __init__(self, text) -> None: ...


class SlashBadAction(Exception):
    def __init__(self, text) -> None: ...


class SlashPatternMismatch(Exception):
    def __init__(self, text) -> None: ...


class SlashLenMismatch(Exception):
    def __init__(self, text) -> None: ...


class SlashOneTableColumn(Exception):
    def __init__(self, text) -> None: ...


class SlashNoResultToFetch(Exception):
    def __init__(self, text) -> None: ...


class SlashUnexpectedError(Exception):
    def __init__(self, text) -> None: ...


class SlashNotTheSame(Exception):
    def __init__(self, text) -> None: ...
