
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .champion import Champion
    from .buff import Buff

from .item import Inventory
#from .rune import Rune


# TODO: this is a container for a Champion, Inventory and Runes
class Summoner:

    def __init__(self, champion: Champion, inventory: Inventory= None) -> None:
        self.champion = champion
        self.inventory = inventory if inventory is not None else Inventory()
        self.current_hp = self.hp
        self.current_buffs = []

    
    # TODO: need to think about how buffs interact with stats etc,
    # how we might gather up bonus stats or effects during attacks.
    def add_buff(self, buff: Buff):
        self.current_buffs.append(buff)

    def remove_buff(self, buff: Buff):
        self.current_buffs.remove(buff)

    @property
    def level(self):
        return self.champion.level

    @property
    def base_ad(self):
        return self.champion.ad

    @property
    def ad(self):
        return self.champion.ad + self.inventory.ad

    #TODO: this will be updated later to reflect when champions can buff there bonus ad.
    @property
    def bonus_ad(self):
        return self.inventory.ad

    @property
    def ap(self):
        return self.champion.ap + self.inventory.ap

    @property
    def base_aspd(self):
        return self.champion.base_aspd

    @property
    def as_ratio(self):
        return self.champion.as_ratio

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

    @property
    def lethality(self):
        return self.inventory.lethality

    @property
    def f_mrp(self):
        return self.inventory.f_mrp

    @property
    def arp(self):
        return self.inventory.arp

    @property
    def mrp(self):
        return self.inventory.mrp




    def __str__(self) -> str:
        return f"{self.champion.name}@{self.champion.level}\n\
                HP   {self.hp}\t\n\
                AD   {self.ad}\tAP {self.ap}\n\
                AR   {self.ar}\tMR {self.mr}\n\
                ASPD {self.aspd}\tAH {self.ah}\n"

