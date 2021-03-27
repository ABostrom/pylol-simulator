from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Any

from .stats import Stats


class Item:
    def __init__(self, name, cost, stat, passives=None) -> None:
        self.name = name
        self.cost = cost
        self.stat = stat
        self.passives = passives if passives != None else []

    def __str__(self) -> str:
        return f"{self.name} | {self.cost}g\n{self.stat}"

    def __repr__(self) -> str:
        return str(self)


class Inventory:

    # deliberately limit constructor to 6 items.
    def __init__(self, item1: Item, item2: Item = None, item3: Item = None,
                 item4: Item = None, item5: Item = None, item6: Item = None) -> None:

        self.items = filter(None, [item1, item2, item3, item4, item5, item6])
        self.current_stats = sum(map(lambda x: x.stat, self.items), Stats())


    # forward the attributes from curent_stats so inventory can be used as a stats object
    # TODO: this feels hacky
    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except:
            return self.current_stats.__dict__[name]

Dagger = Item("Dagger", 300, Stats(aspd=25))
Long_Sword = Item("Long Sword", 350, Stats(ad=10))

from .modifiers import SteelTipped
RecurveBow = Item("Recurve Bow", 1000, Stats(aspd=25), passives=[SteelTipped()])


