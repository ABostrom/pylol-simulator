
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .champion import Champion

from .item import Inventory
#from .rune import Rune


# TODO: this is a container for a Champion, Inventory and Runes
class Summoner:

    def __init__(self, champion: Champion, inventory: Inventory= None) -> None:
        self.champion = champion
        self.inventory = inventory if inventory is not None else Inventory()
        self.current_hp = self.hp

    @property
    def base_ad(self):
        return self.champion.ad

    @property
    def ad(self):
        return self.champion.ad + self.inventory.ad

    @property
    def ap(self):
        return self.champion.ap + self.inventory.ap

    @property
    def base_aspd(self):
        return self.champion.base_aspd

    @property
    def aspd(self):
        return self.champion.aspd + self.inventory.aspd

    @property
    def cs(self):
        return self.champion.cs + self.inventory.cs

    @property
    def csd(self):
        return self.champion.csd + self.inventory.csd

    @property
    def ah(self):
        return self.champion.ah + self.inventory.ah

    @property
    def ar(self):
        return self.champion.ar + self.inventory.ar

    @property
    def mr(self):
        return self.champion.mr + self.inventory.mr

    @property
    def hp(self):
        return self.champion.hp + self.inventory.hp


    def __str__(self) -> str:
        return f"{self.champion.name}@{self.champion.level}\nAD   {self.ad}\tAP {self.ap}\nAR   {self.ar}\tMR {self.mr}\nASPD {self.aspd}\tAH {self.ah}\n"

