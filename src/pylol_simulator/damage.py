# from enum import Enum

# class DamageTypes(Enum):
#     TRUE = 0
#     PHYSICAL = 1
#     MAGIC = 2

from .champion_stats import ChampionBaseStats, Stats

class Damage:

    def __init__(self, true_damage:float = 0, physical_damage:float = 0, magic_damage:float = 0) -> None:
        self.true = true_damage
        self.physical = physical_damage
        self.magic = magic_damage


# this formula is the same for armour and magic resistance
def calculate_mitigation(damage:float, resist:float):
    return 100 / (100 + resist) * damage



def basic_attack(base_stats:ChampionBaseStats, bonus_stats:Stats, champion_lvl:int=1, time:float=0):

    damage = base_stats.as

    return Damage(physical_damage=damage)