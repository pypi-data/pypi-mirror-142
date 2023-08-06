import dataclasses
import typing


@dataclasses.dataclass
class Product:
    name: str
    version: str
    comments: typing.List[str] = dataclasses.field(default_factory=list)

    def __str__(self) -> str:
        return str(self.identifier) + (
            " ({comment})".format(
                comment="; ".join(self.comments),
            )
            if self.comments
            else ""
        )

    @property
    def identifier(self) -> str:
        return f"{self.name}/{self.version}"


@dataclasses.dataclass
class UserAgent:
    products: typing.List[Product]

    def __str__(self) -> str:
        return " ".join(map(str, self.products))

    def __iter__(self) -> typing.Iterable[Product]:
        product: Product
        for product in self.products:
            yield product
