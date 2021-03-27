# from enum import Enum

# class DamageTypes(Enum):
#     TRUE = 0
#     PHYSICAL = 1
#     MAGIC = 2

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .summoner import Summoner

class Damage:

    def __init__(self, true_damage:float = 0, physical_damage:float = 0, magic_damage:float = 0) -> None:
        self.true = true_damage
        self.physical = physical_damage
        self.magic = magic_damage

    def __add__(self, other):
        return Damage(self.true+other.true, self.physical+other.physical, self.magic+other.magic)

    def get_total_damage(self):
        return self.true + self.physical + self.magic
        


# this formula is the same for armour and magic resistance
def calculate_mitigation(damage:float, resist:float):
    return 100 / (100 + resist) * damage


def calculate_apsd(base_aspd, bonus_aspd):
    return base_aspd * (1 + bonus_aspd / 100)

def basic_attack(summoner: Summoner):
    # basic attacks are 100% of total ad.

    # TODO: Crit chance/Crit Damage
    # TODO: trigger on hit passives
    damage = summoner.ad #+ summoner.

    return Damage(physical_damage=damage)


time_since_last_attack = 0
last_time = 0
def swing_timer(summoner: Summoner, time:float=0):

    global last_time
    global time_since_last_attack

    #reset the swing timer if this is a new call.
    if time <= 0:
        last_time = 0
        time_since_last_attack = 0

    #keep an internal record of the swing timer.
    delta_time = time - last_time
    time_since_last_attack += delta_time

    # need to check the swing timer, against this frequency
    # TODO: tidy up this with bonus aspd from summoner.
    frequency = 1.0 / calculate_apsd(summoner.base_aspd, summoner.aspd)

    # if its been longer than our freqency since our last attack, we're good to go.
    # or if time is 0 then we can attack instantly.
    if time_since_last_attack >=  frequency or time_since_last_attack == 0:

        damage = basic_attack(summoner)
        #reset the swing timer.
        time_since_last_attack = 0
    else:
        damage = Damage()
    
    last_time = time

    return damage





