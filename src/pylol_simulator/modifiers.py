
from __future__ import annotations
from typing import TYPE_CHECKING

from numpy.lib.arraysetops import unique
if TYPE_CHECKING:
    from .summoner import Summoner

from .damage import Damage


class Passive:

    def __init__(self, name:str, unique:bool) -> None:
        self.name = name
        self.unique = unique

    # called when the owner of this item attacks
    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        pass

    # called when the owner of this item casts an ability
    def on_ability_used(): 
        pass

    def __eq__(self, o: Passive) -> bool:
        return self.name == o.name and (self.unique or o.unique)

    def __hash__(self) -> int:
        return hash((self.name, self.unique))

'''Recurve Bow Passives'''

class SteelTipped(Passive):

    def __init__(self) -> None:
        super().__init__("Steel Tipped", True)

    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        return Damage(physical_damage=15)


'''Nashor's Tooth Passives'''

class IcathianBite(Passive):
    def __init__(self) -> None:
        super().__init__("Icathian Bite", True)

    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        return Damage(magic_damage = 15 + (attacker.ap * 0.2))



'''Blade of the Ruined Kind Passives'''

#TODO: Program the disinction between range and melee
class MistsEdge(Passive):
    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        #TODO: Cap this to 60 against minions and monsters.
        return Damage(physical_damage=defender.current_hp*0.1)

class Siphon(Passive): 
    def __init__(self, name:str, unique:bool) -> None:
        super().__init__(name, unique)
        self.atack_count = 0 


    # TODO: Need a buff/debuff system
    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        pass



'''Sheen Passive'''
class SpellBlade(Passive):

    # TODO: consider how these effects timeout.
    def __init__(self) -> None:
        super().__init__("Spell Blade", True)
        self.active = False

    def on_ability_used(self): 
        self.active = True

    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        damage = 0
        if self.active:
            damage = attacker.base_ad

        self.active = False
        return Damage(physical_damage=damage)



class BringItDown(Passive):
    # TODO: consider how these effects/stacks timeout.
    # TODO: probs need a buff/debuffs system
    def __init__(self) -> None:
        super().__init__("Bring It Down", True)
        self.count = 0

    def on_basic_attack(self, attacker:Summoner, defender:Summoner):
        tr_damage = 0
        if self.count >= 2:
            self.count = 0
            tr_damage = 60 + (0.45 * attacker.bonus_ad)
        else:
            self.count += 1

        return Damage(true_damage=tr_damage)