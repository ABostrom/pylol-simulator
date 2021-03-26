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



time_since_last_attack = 0
last_time = 0

def basic_attack(base_stats:ChampionBaseStats, bonus_stats:Stats, champion_lvl:int=1, time:float=0):

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
    frequency = 1.0 / (base_stats.aspd * (1 + bonus_stats.aspd / 100))

    # if its been longer than our freqency since our last attack, we're good to go.
    # or if time is 0 then we can attack instantly.
    if time_since_last_attack >=  frequency or time_since_last_attack == 0:
         # basic attacks are 100% of total ad.
        damage = base_stats.ad + bonus_stats.ad

        #reset the swing timer.
        time_since_last_attack = 0
    else:
        damage = 0
    
    last_time = time

    return Damage(physical_damage=damage)