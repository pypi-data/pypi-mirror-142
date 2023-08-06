import enum


class ProductName(str, enum.Enum):
    MOZILLA: str = "Mozilla"
    GECKO: str = "Gecko"
    FIREFOX: str = "Firefox"
