from __future__ import annotations
from typing import List, TYPE_CHECKING

from numpy.core.numeric import _outer_dispatcher
if TYPE_CHECKING:
    from typing import Any
    from .modifiers import Passive

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
    def __init__(self, item1: Item=None, item2: Item = None, item3: Item = None,
                 item4: Item = None, item5: Item = None, item6: Item = None) -> None:

        self.items = list(filter(None, [item1, item2, item3, item4, item5, item6]))
        self.current_stats = sum(map(lambda x: x.stat, self.items), Stats())


    def get_all_unique_passives(self) -> List[Passive]:
        out = set()
        for item in self.items:
            out.add(*item.passives)
        return list(out)



    # forward the attributes from curent_stats so inventory can be used as a stats object
    # TODO: this feels hacky
    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except:
            return self.current_stats.__dict__[name]

from .modifiers import SteelTipped
from .modifiers import IcathianBite
from .modifiers import SpellBlade
from .modifiers import BringItDown
from .modifiers import GiantSlayer

'''AD Base Items'''
Long_Sword = Item("Long Sword", 350, Stats(ad=10))
Pickaxe = Item("Pickaxe", 875, Stats(ad=25))
BFSword = Item("B. F. Sword", 1300, Stats(ad=40))

'''AP Base Items'''
AmplifyingTome = Item("Amplifying Tome", 350, Stats(ap=20))
BlastingWand = Item("Blasting Wand", 850, Stats(ap=40))
NeedlesslyLargeRod = Item("Needlessly Large Rod", 1300, Stats(ap=60))

'''ASPD Base Items'''
Dagger = Item("Dagger", 300, Stats(aspd=25))
RecurveBow = Item("Recurve Bow", 1000, Stats(aspd=25), passives=[SteelTipped()])

'''Crit Chance'''
CloakOfAgility = Item("Cloak of Agility", 600, Stats(cs=15))

'''Hp'''
RubyCrystal = Item("Ruby Crystal", 400, Stats(hp=150))
GiantsBelt = Item("Giant's Belt", 900, Stats(hp=350))

'''Armour '''
ClothArmor = Item("Cloth Armor", 300, Stats(ar=15))
ChainVest = Item("Chain Vest", 800, Stats(ar=40))

'''Magic Resist'''
NullMagicMantle = Item("Null-Magic Mantle", 450, Stats(mr=25))
NegatronCloak = Item("Negatron Cloak", 900, Stats(mr=50))

'''marksmen items'''
KrakenSlayer = Item("Kraken Slayer", 3400, Stats(ad=65, aspd=25, cs=20), passives=[BringItDown()])
LordDominiksRegards = Item("Lord Dominik's Regards", 3000, Stats(ad=30,cs=20,arp=35), passives=[GiantSlayer()])

Sheen = Item("Sheen", 700, Stats(), passives=[SpellBlade()])

NashorsTooth = Item("Nashor's Tooth", 3000, Stats(ap=100, aspd=50), passives=[IcathianBite()])
