
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .summoner import Summoner

from .damage import Damage


class Passive:

    def __init__(self, name:str, unique:bool) -> None:
        self.name = name
        self.unique = unique

    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        pass

class SteelTipped:
    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        return Damage(physical_damage=15)


