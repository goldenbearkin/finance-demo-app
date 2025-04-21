from typing import Final

TRILLION: Final[float] = 1_000_000_000_000
BILLION: Final[float] = 1_000_000_000
MILLION: Final[float] = 1_000_000
THOUSAND: Final[float] = 1_000


def to_shorter_number(number: float) -> str:
    abs_number = abs(number)

    if abs_number >= TRILLION:
        return f"{number / TRILLION:.2f}T"
    elif abs_number >= BILLION:
        return f"{number / BILLION:.2f}B"
    elif abs_number >= MILLION:
        return f"{number / MILLION:.2f}M"
    elif abs_number >= THOUSAND:
        return f"{number / THOUSAND:.2f}K"
    elif number.is_integer():
        return str(int(number))
    else:
        return f"{number:.2f}"
