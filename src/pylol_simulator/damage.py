# from enum import Enum

# class DamageTypes(Enum):
#     TRUE = 0
#     PHYSICAL = 1
#     MAGIC = 2

from .champion import Champion
from .item import Inventory

class Damage:

    def __init__(self, true_damage:float = 0, physical_damage:float = 0, magic_damage:float = 0) -> None:
        self.true = true_damage
        self.physical = physical_damage
        self.magic = magic_damage

    
    def get_total_damage(self):
        return self.true + self.physical + self.magic
        


# this formula is the same for armour and magic resistance
def calculate_mitigation(damage:float, resist:float):
    return 100 / (100 + resist) * damage


def calculate_apsd(base_aspd, bonus_aspd):
    return base_aspd * (1 + bonus_aspd / 100)

def basic_attack(champion:Champion, inventory: Inventory):
    # basic attacks are 100% of total ad.

    # TODO: Crit chance/Crit Damage
    damage = champion.get_ad() + inventory.current_stats.ad

    return Damage(physical_damage=damage)


time_since_last_attack = 0
last_time = 0
def swing_timer(champion:Champion, inventory:Inventory, time:float=0):

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
    frequency = 1.0 / calculate_apsd(champion.get_base_aspd(), inventory.aspd + champion.get_bonus_aspd())

    # if its been longer than our freqency since our last attack, we're good to go.
    # or if time is 0 then we can attack instantly.
    if time_since_last_attack >=  frequency or time_since_last_attack == 0:

        damage = basic_attack(champion, inventory)
        #reset the swing timer.
        time_since_last_attack = 0
    else:
        damage = Damage()
    
    last_time = time

    return damage





