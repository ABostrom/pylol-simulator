

from .stats import Stats



class Item(object):
    def __init__(self, name, cost, stat, passive=None) -> None:
        self.name= name
        self.cost = cost
        self.stat = stat


    def __str__(self) -> str:
        return f"{self.name} | {self.cost}g\n{self.stat}"

    def __repr__(self) -> str:
        return str(self)


Dagger = Item("Dagger", 300, Stats(aspd=25))
Long_Sword = Item("Long Sword", 350, Stats(ad=10))