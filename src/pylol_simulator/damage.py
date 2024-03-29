# from enum import Enum

# class DamageTypes(Enum):
#     TRUE = 0
#     PHYSICAL = 1
#     MAGIC = 2

from __future__ import annotations

import random
from typing import TYPE_CHECKING
from random import randint

from pylol_simulator.champion import TargetDummy

if TYPE_CHECKING:
    from .summoner import Summoner
    from .item import Inventory


class Damage:

    def __init__(self, true_damage: float = 0, physical_damage: float = 0, magic_damage: float = 0) -> None:
        self.true = true_damage
        self.physical = physical_damage
        self.magic = magic_damage

    def __add__(self, other):
        return Damage(self.true + other.true, self.physical + other.physical, self.magic + other.magic)

    def critical_strike(self):
        self.true = self.true*1.75
        self.physical = self.physical*1.75
        self.magic = self.magic*1.75
        pass

    def get_total_damage(self):
        return self.true + self.physical + self.magic

    def __str__(self) -> str:
        return f"Total:\t{self.get_total_damage()}\nTrue:\t{self.true}\nPhys:\t{self.physical}\nMagic:\t{self.magic}"

    def get_mitigated_damage(self, attacker: Summoner, defender: Summoner) -> Damage:
        # TODO: Consider about armour reduction, and base armour + bonus armour
        d_ar = (defender.ar * (1 - (attacker.arp / 100))) - calculate_flat_armour_pen(attacker.lethality,
                                                                                      attacker.level)

        # TODO: Consider how magic pen interacts with magic resist
        d_mr = (defender.mr * (1 - (attacker.mrp / 100))) - attacker.f_mrp

        return Damage(physical_damage=calculate_mitigation(self.physical, d_ar),
                      magic_damage=calculate_mitigation(self.magic, d_mr),
                      true_damage=self.true)


def calculate_flat_armour_pen(lethality: float, level: int):
    return lethality * (0.6 + 0.4 * level / 18)


# this formula is the same for armour and magic resistance
def calculate_mitigation(damage: float, resist: float):
    return 100 / (100 + resist) * damage


def calculate_apsd(base_aspd, as_ratio, bonus_aspd):
    return base_aspd + (as_ratio * bonus_aspd / 100)

def calculate_crit(cs):
    value = random.random()
    print(value, cs)
    return value < cs






def basic_attack(attacker: Summoner, defender: Summoner):
    # basic attacks are 100% of total ad.

    # TODO: Crit chance/Crit Damage
    # TODO: trigger on hit passives
    # TODO: consider how buffs interact here too.
    # attacker.current_buffs
    basic = Damage(physical_damage=attacker.ad)
    passives = attacker.inventory.get_all_unique_passives()
    output = basic + sum([passive.on_basic_attack(attacker, defender) for passive in passives], Damage())
    if calculate_crit(attacker.cs):
        output.critical_strike()
        print("CRIT HIT")
    mitigated_output = output.get_mitigated_damage(attacker, defender)

    return mitigated_output


time_since_last_attack = 0
last_time = 0


def swing_timer(attacker: Summoner, defender: Summoner, time: float = 0):
    global last_time
    global time_since_last_attack

    # reset the swing timer if this is a new call.
    if time <= 0:
        last_time = 0
        time_since_last_attack = 0

    # keep an internal record of the swing timer.
    delta_time = time - last_time
    time_since_last_attack += delta_time

    # need to check the swing timer, against this frequency
    frequency = 1.0 / calculate_apsd(attacker.base_aspd, attacker.as_ratio, attacker.aspd)

    # if its been longer than our freqency since our last attack, we're good to go.
    # or if time is 0 then we can attack instantly.
    if time_since_last_attack >= frequency or time_since_last_attack == 0:

        damage = basic_attack(attacker, defender)
        # reset the swing timer.
        time_since_last_attack = 0
    else:
        damage = Damage()

    last_time = time

    return damage
