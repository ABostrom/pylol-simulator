from __future__ import annotations

import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .summoner import Summoner
    from .buff import Buff

from .damage import Damage


class Passive:

    def __init__(self, name: str, unique: bool) -> None:
        self.name = name
        self.unique = unique

    # called when the owner of this item attacks
    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        pass

    # called when the owner of this item casts an ability
    def on_ability_used(attacker: Summoner):
        pass

    def __eq__(self, o: Passive) -> bool:
        return self.name == o.name and (self.unique or o.unique)

    def __hash__(self) -> int:
        return hash((self.name, self.unique))


class SpawnBuff(Passive):
    def __init__(self, toSpawn: Buff) -> None:
        super().__init__("Spawn Buff", False)
        self.buff = toSpawn

    def on_ability_used(self, attacker: Summoner):
        attacker.add_buff(self.toSpawn)


'''Recurve Bow Passives'''


class SteelTipped(Passive):

    def __init__(self) -> None:
        super().__init__("Steel Tipped", True)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        return Damage(physical_damage=15)


'''Nashor's Tooth Passives'''


class IcathianBite(Passive):
    def __init__(self) -> None:
        super().__init__("Icathian Bite", True)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        return Damage(magic_damage=15 + (attacker.ap * 0.2))


'''Blade of the Ruined Kind Passives'''


class BringItDown(Passive):
    # TODO: consider how these effects/stacks timeout.
    # TODO: probs need a buff/debuffs system
    def __init__(self) -> None:
        super().__init__("Bring It Down", True)
        self.count = 0

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        tr_damage = 0
        if self.count >= 2:
            self.count = 0
            tr_damage = 60 + (0.45 * attacker.bonus_ad)
        else:
            self.count += 1

        return Damage(true_damage=tr_damage)


class EverRisingMoon(Passive):

    def __init__(self, ability_delay) -> None:
        super().__init__("Ever Rising Moon", True)
        self.last_hit = -1
        self.max_next_hit_delay = -1
        self.delay_time = ability_delay

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        # First Attack of the time-frame.
        if self.last_hit == -1 or self.max_next_hit_delay == -1:
            self.last_hit = time.perf_counter()
            self.max_next_hit_delay = self.last_hit + self.delay_time
        else:
            # Is a valid hit within 'self.delay_time' or 1.5 seconds.
            if time.perf_counter() <= self.max_next_hit_delay:
                return Damage(true_damage=attacker.base_ad + (defender.hp * 0.06))
            self.last_hit = -1
            self.max_next_hit_delay = -1


class Lifeline(Passive):

    def __init__(self):
        super().__init__("Lifeline", True)

    def get_shield_based_on_level(self, level):
        data_points = [250, 292.22, 334.44, 376.67, 418.89, 461.11, 503.33, 545.56, 587.78, 630]
        if level < 10:
            return data_points[0]
        else:
            return data_points[level - 10]

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        # Get Thirty Percent (used for check)
        thirty_percent_of_max_health = defender.hp * 0.3
        # If current_hp - damage < thirty_percent_of_max_hp
        if defender.current_hp - attacker.base_ad < thirty_percent_of_max_health:
            # Get shield for level (250-630 depending on level)
            shield = self.get_shield_based_on_level(defender.level)
            # Offset the damage "absorbed by shield" - also, max the value to 0, to avoid negative values of damage.
            return Damage(physical_damage=max(attacker.base_ad - shield, 0))
        else:
            # The attack isn't less than 30% of the max hp, so just return the damage.
            return Damage(physical_damage=attacker.base_ad)


class Fray(Passive):

    def __init__(self):
        super().__init__("Fray", True)

    def get_bonus_magic_damage_based_on_level(self, level):
        data = [15, 25, 35, 45, 55, 65, 75, 76.25, 77.5, 78.75, 80]
        if level < 9:
            return data[0]
        else:
            return data[level - 9]

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        # Get bonus damage based on level.
        bonus_damage = self.get_bonus_magic_damage_based_on_level(defender.level)
        return Damage(magic_damage=bonus_damage)


class GiantSlayer(Passive):

    def __init__(self) -> None:
        super().__init__("Giant Slayer", True)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        health_diff = min(max(defender.hp - attacker.hp, 0), 2000)  # clamp to 2000 health max difference
        damage = int(health_diff / 100) * 0.0075 * health_diff
        return Damage(physical_damage=damage)


class MistsEdge(Passive):

    def __init__(self):
        super().__init__("Mist's Edge", True)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        # If the current_hp isn't an integer or float (warning messages due to inferred types)
        if not isinstance(defender.current_hp, (int, float)):
            return Damage(physical_damage=attacker.base_ad)
        # Return boost onto base attack damage for 8% of the defenders' current hp.
        return Damage(physical_damage=attacker.base_ad + (defender.current_hp * 0.08))


class Siphon(Passive):

    def __init__(self):
        super().__init__("Siphon", True)
        self.start = -1
        self.end = -1
        self.delay = 6
        self.required_hits_before_use = 3
        self.stacked_hits = 0

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        if self.start == -1 or self.end == -1:  # No hit to start stack yet.
            self.start = time.perf_counter()
            self.end = self.start + self.delay
            self.stacked_hits += 1
        else:  # Has a stack.
            if time.perf_counter() <= self.end:  # If hit is within 6 seconds.
                self.stacked_hits += 1
                # Has hit '3' hits in '6' seconds to then do the magical hit of epicness.
                if self.stacked_hits != self.required_hits_before_use:
                    return Damage(physical_damage=attacker.base_ad)
                else:
                    self.stacked_hits = 0
                    self.start = -1
                    self.end = -1
                    #                                                             40 + 110 / 17 * (level - 1)
                    return Damage(physical_damage=attacker.base_ad, magic_damage=(40 + 110 / 17 * (attacker.level - 1)))
            self.stacked_hits = 0
            self.start = -1
            self.end = -1
        return Damage(physical_damage=attacker.base_ad)


class SpectralWaltz(Passive):

    def __init__(self):
        super().__init__("Spectral Waltz", True)
        self.start = -1
        self.end = -1
        self.delay = 3
        self.stacks = 0
        self.stacks_required = 4

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        if self.start == -1 or self.end == -1:  # No hit to start stack yet.
            self.start = time.perf_counter()
            self.end = self.start + self.delay
            self.stacks += 1
        else:  # Has a stack.
            if time.perf_counter() <= self.end:  # If hit is within 3 seconds.
                self.stacks += 1
                # Has hit '4' hits in '3' seconds to then give a bonus attack speed boost.
                if self.stacks == self.stacks_required:
                    self.stacks = 0
                    self.start = -1
                    self.end = -1
                    attacker.champion.base_aspd += attacker.champion.base_aspd * 0.3
                    return Damage(physical_damage=attacker.base_ad)
                else:
                    return Damage(physical_damage=attacker.base_ad)
            self.stacks = 0
            self.start = -1
            self.end = -1
            attacker.champion.base_aspd -= attacker.champion.base_aspd * 0.3
        return Damage(physical_damage=attacker.base_ad)


class Energized(Passive):

    def __init__(self):
        super().__init__("Energized", True)
        self.attack_stacks = 6

    # noinspection PyUnresolvedReferences
    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        # Using the custom runtime attribute methods created in Summoner, create the new attribute 'energy' which stores
        # the Summoners' energy levels for the passive 'Energized'.
        if not attacker.has_runtime_attribute("energy"):
            attacker.runtime_attribute("energy", 0)
        attacker.energy += self.attack_stacks  # Increments new custom statistic.
        # If its 100, do the bonus magic and then reset the energy value.
        if attacker.energy >= 100:
            attacker.energy = 0
            bonus = 120
        else:
            bonus = 0
        return Damage(physical_damage=attacker.base_ad, magic_damage=bonus)


class Sharpshooter(Passive):

    def __init__(self):
        super().__init__("Energized", True)
        self.minimum_required_energy = 100

    # noinspection PyUnresolvedReferences
    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        if not attacker.has_runtime_attribute("energy"):
            attacker.runtime_attribute("energy", 0)
        return Damage(physical_damage=attacker.base_ad,
                      magic_damage=120 if attacker.energy >= self.minimum_required_energy else 0)

# TODO refine these to check for mythicality.
class DivineSundererMythic(Passive):

    def __init__(self):
        super().__init__("MYTHIC PASSIVE", False)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        attacker.champion.ap += attacker.champion.ap * 0.05
        attacker.champion.mrp += attacker.champion.mrp * 0.05
        return Damage(physical_damage=attacker.base_ad)

class KrakenSlayerMythic(Passive):

    def __init__(self):
        super().__init__("MYTHIC PASSIVE", False)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        attacker.champion.apsd += attacker.champion.apsd * 0.1
        return Damage(physical_damage=attacker.base_ad)

class ImmortalShieldbowMythic(Passive):

    def __init__(self):
        super().__init__("MYTHIC PASSIVE", False)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        attacker.champion.base_stats.ad += attacker.champion.base_stats.ad + 5
        attacker.champion.base_stats.hp += attacker.champion.base_stats.hp + 70
        return Damage(physical_damage=attacker.base_ad)

class TrinityForceMythic(Passive):

    def __init__(self):
        super().__init__("MYTHIC PASSIVE", False)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        attacker.champion.base_stats.ad += attacker.champion.base_stats.ad + 3
        attacker.champion.base_stats.aspd += attacker.champion.base_stats.aspd + 3
        return Damage(physical_damage=attacker.base_ad)

class EclipseMythic(Passive):

    def __init__(self):
        super().__init__("MYTHIC PASSIVE", False)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        attacker.champion.base_stats.ap += attacker.champion.base_stats.ap * 0.04
        return Damage(physical_damage=attacker.base_ad)

