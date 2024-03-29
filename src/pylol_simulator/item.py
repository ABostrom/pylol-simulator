from __future__ import annotations

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
from .modifiers import *
from .stats import Stats


class Item:
    def __init__(self, name, cost, stat, passives=None, mythic=False, legendary=False) -> None:
        self.name = name
        self.cost = cost
        self.stat = stat
        self.passives = passives if passives is not None else []
        self.mythic = mythic
        self.legendary = legendary

    def __str__(self) -> str:
        return f"{self.name} | {self.cost}g\n{self.stat}"

    def __repr__(self) -> str:
        return str(self)


class Inventory:

    # deliberately limit constructor to 6 items.
    def __init__(self, item1: Item = None, item2: Item = None, item3: Item = None,
                 item4: Item = None, item5: Item = None, item6: Item = None) -> None:

        self.items = list(filter(None, [item1, item2, item3, item4, item5, item6]))
        mythics_in_inventory = [item for item in self.items if item.mythic]
        if len(mythics_in_inventory) > 1:
            print("Found more than 1 mythic in inventory, removing all but the first one.")
            for index in range(1, len(mythics_in_inventory)):
                self.items.remove(mythics_in_inventory[index])
        self.current_stats = sum(map(lambda x: x.stat, self.items), Stats())

    def get_all_unique_passives(self) -> List[Passive]:
        out = set()
        for item in self.items:
            # this is causing an error if an item does not have passives, fixed with if statement below
            if len(item.passives) != 0:
                out.add(*item.passives)
        return list(out)

    # forward the attributes from curent_stats so inventory can be used as a stats object
    # TODO: this feels hacky
    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except:
            return self.current_stats.__dict__[name]


from .modifiers import SteelTipped
from .modifiers import IcathianBite
from .modifiers import SpawnBuff
from .modifiers import BringItDown
from .modifiers import GiantSlayer

'''AD Base Items'''
Long_Sword = Item("Long Sword", 350, Stats(ad=10))
Pickaxe = Item("Pickaxe", 875, Stats(ad=25))
BFSword = Item("B. F. Sword", 1300, Stats(ad=40))

'''AP Base Items'''
AmplifyingTome = Item("Amplifying Tome", 350, Stats(ap=20))
BlastingWand = Item("Blasting Wand", 850, Stats(ap=40))
NeedlesslyLargeRod = Item("Needlessly Large Rod", 1250, Stats(ap=60))

'''ASPD Base Items'''
Dagger = Item("Dagger", 300, Stats(aspd=25))
RecurveBow = Item("Recurve Bow", 1000, Stats(aspd=25), passives=[SteelTipped()])

'''cs Chance'''
CloakOfAgility = Item("Cloak of Agility", 600, Stats(cs=15))

'''Hp'''
RubyCrystal = Item("Ruby Crystal", 400, Stats(hp=150))
GiantsBelt = Item("Giant's Belt", 900, Stats(hp=350))

'''Armour '''
ClothArmor = Item("Cloth Armor", 300, Stats(ar=15))
ChainVest = Item("Chain Vest", 800, Stats(ar=40))

'''Magic Resist'''
NullMagicMantle = Item("Null-Magic Mantle", 450, Stats(mr=25))
NegatronCloak = Item("Negatron Cloak", 900, Stats(mr=50))

'''marksmen items'''
KrakenSlayer = Item("Kraken Slayer", 3400, Stats(ad=65, aspd=25, cs=20), passives=[BringItDown()])
LordDominiksRegards = Item("Lord Dominik's Regards", 3000, Stats(ad=30, cs=20, arp=35), passives=[GiantSlayer()])
# ImmortalShieldBow = Item("Immortal Shieldbow", 3400, Stats(ad=50, aspd=20, cs=20, ls=10), passives=[Lifeline])

''' Sheen Items '''
from .buff import SheenSpellBlade, TriforceSpellBlade, LichBaneSpellBlade

Sheen = Item("Sheen", 700, Stats(), passives=[SpawnBuff(toSpawn=SheenSpellBlade())])
Triforce = Item("Trinity Force", 3333, Stats(ad=30, ah=20, aspd=30, hp=200),
                passives=[SpawnBuff(toSpawn=TriforceSpellBlade())])
# TODO: MS
LichBane = Item("Lich Bane", 3000, Stats(ap=70), passives=[SpawnBuff(toSpawn=LichBaneSpellBlade())])

NashorsTooth = Item("Nashor's Tooth", 3000, Stats(ap=100, aspd=50), passives=[IcathianBite()])

# Autogenerated.
Boots = Item("Boots", 300, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Faerie_Charm = Item("Faerie Charm", 250, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Rejuvenation_Bead = Item("Rejuvenation Bead", 300, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Giants_Belt = Item("Giant's Belt", 900, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=350, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Cloak_of_Agility = Item("Cloak of Agility", 600, Stats(ad=0, ap=0, aspd=0, cs=15, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Blasting_Wand = Item("Blasting Wand", 850, Stats(ad=0, ap=40, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Sapphire_Crystal = Item("Sapphire Crystal", 350, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=250, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Ruby_Crystal = Item("Ruby Crystal", 400, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Cloth_Armor = Item("Cloth Armor", 300, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=15,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Chain_Vest = Item("Chain Vest", 800, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=40,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
NullMagic_Mantle = Item("Null-Magic Mantle", 450, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=25, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Emberknife = Item("Emberknife", 350, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Long_Sword = Item("Long Sword", 350, Stats(ad=10, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Pickaxe = Item("Pickaxe", 875, Stats(ad=25, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
B_F_Sword = Item("B. F. Sword", 1300, Stats(ad=40, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Hailblade = Item("Hailblade", 350, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Obsidian_Edge = Item("Obsidian Edge", 350, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Dagger = Item("Dagger", 300, Stats(ad=0, ap=0, aspd=12, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Amplifying_Tome = Item("Amplifying Tome", 435, Stats(ad=0, ap=20, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Vampiric_Scepter = Item("Vampiric Scepter", 900, Stats(ad=15, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=10))
Dorans_Shield = Item("Doran's Shield", 450, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=80, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Dorans_Blade = Item("Doran's Blade", 450, Stats(ad=8, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=80, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Dorans_Ring = Item("Doran's Ring", 400, Stats(ad=0, ap=15, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=70, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Negatron_Cloak = Item("Negatron Cloak", 900, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=50, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Needlessly_Large_Rod = Item("Needlessly Large Rod", 1250, Stats(ad=0, ap=60, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Dark_Seal = Item("Dark Seal", 350, Stats(ad=0, ap=15, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=40, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Cull = Item("Cull", 450, Stats(ad=7, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Health_Potion = Item("Health Potion", 50, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Total_Biscuit_of_Everlasting_Will = Item("Total Biscuit of Everlasting Will", 50, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Kircheis_Shard = Item("Kircheis Shard", 700, Stats(ad=0, ap=0, aspd=15, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Refillable_Potion = Item("Refillable Potion", 150, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Corrupting_Potion = Item("Corrupting Potion", 500, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Guardians_Horn = Item("Guardian's Horn", 950, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
PoroSnax = Item("Poro-Snax", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Control_Ward = Item("Control Ward", 75, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Shurelyas_Battlesong = Item("Shurelya's Battlesong", 2500, Stats(ad=0, ap=40, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Elixir_of_Iron = Item("Elixir of Iron", 500, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Elixir_of_Sorcery = Item("Elixir of Sorcery", 500, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Elixir_of_Wrath = Item("Elixir of Wrath", 500, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Minion_Dematerializer = Item("Minion Dematerializer", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Commencing_Stopwatch = Item("Commencing Stopwatch", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Stopwatch = Item("Stopwatch", 650, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Broken_Stopwatch = Item("Broken Stopwatch", 650, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Slightly_Magical_Footwear = Item("Slightly Magical Footwear", 300, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Perfectly_Timed_Stopwatch = Item("Perfectly Timed Stopwatch", 650, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Broken_Stopwatch = Item("Broken Stopwatch", 650, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Evenshroud = Item("Evenshroud", 2500, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=30,
        mr=30, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Archangels_Staff = Item("Archangel's Staff", 2600, Stats(ad=0, ap=60, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=200, mana=500, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Manamune = Item("Manamune", 2900, Stats(ad=35, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=0, mana=500, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Berserkers_Greaves = Item("Berserker's Greaves", 1100, Stats(ad=0, ap=0, aspd=35, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Boots_of_Swiftness = Item("Boots of Swiftness", 900, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Chemtech_Putrifier = Item("Chemtech Putrifier", 2300, Stats(ad=0, ap=55, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Sorcerers_Shoes = Item("Sorcerer's Shoes", 1100, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=18, ls=0))
Glacial_Buckler = Item("Glacial Buckler", 900, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=20,
        mr=0, hp=0, mana=250, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Guardian_Angel = Item("Guardian Angel", 2800, Stats(ad=40, ap=0, aspd=0, cs=0, ah=0, ar=40,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Infinity_Edge = Item("Infinity Edge", 3400, Stats(ad=70, ap=0, aspd=0, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Mortal_Reminder = Item("Mortal Reminder", 2500, Stats(ad=25, ap=0, aspd=25, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Last_Whisper = Item("Last Whisper", 1450, Stats(ad=20, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=20, mrp=0, lethality=0, f_mrp=0, ls=0))
Seraphs_Embrace = Item("Seraph's Embrace", 2600, Stats(ad=0, ap=80, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=250, mana=860, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Mejais_Soulstealer = Item("Mejai's Soulstealer", 1600, Stats(ad=0, ap=20, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=100, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Muramana = Item("Muramana", 3000, Stats(ad=35, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=0, mana=860, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Phage = Item("Phage", 1100, Stats(ad=15, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Phantom_Dancer = Item("Phantom Dancer", 2600, Stats(ad=20, ap=0, aspd=25, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Plated_Steelcaps = Item("Plated Steelcaps", 1100, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=20,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Zekes_Convergence = Item("Zeke's Convergence", 2400, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=25,
        mr=0, hp=250, mana=250, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Hearthbound_Axe = Item("Hearthbound Axe", 1000, Stats(ad=15, ap=0, aspd=15, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Steraks_Gage = Item("Sterak's Gage", 3100, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=400, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Spirit_Visage = Item("Spirit Visage", 2900, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=0,
        mr=40, hp=450, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Winged_Moonplate = Item("Winged Moonplate", 800, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Kindlegem = Item("Kindlegem", 800, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Sunfire_Aegis = Item("Sunfire Aegis", 3200, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=35,
        mr=35, hp=350, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Tear_of_the_Goddess = Item("Tear of the Goddess", 400, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=240, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Black_Cleaver = Item("Black Cleaver", 3100, Stats(ad=45, ap=0, aspd=0, cs=0, ah=30, ar=0,
        mr=0, hp=350, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Bloodthirster = Item("Bloodthirster", 3400, Stats(ad=55, ap=0, aspd=0, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=20), legendary=True)
Ravenous_Hydra = Item("Ravenous Hydra", 3300, Stats(ad=70, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Thornmail = Item("Thornmail", 2700, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=60,
        mr=0, hp=350, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Bramble_Vest = Item("Bramble Vest", 800, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=30,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Tiamat = Item("Tiamat", 1200, Stats(ad=25, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Wardens_Mail = Item("Warden's Mail", 1000, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=40,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Warmogs_Armor = Item("Warmog's Armor", 3000, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=0,
        mr=0, hp=800, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Runaans_Hurricane = Item("Runaan's Hurricane", 2600, Stats(ad=0, ap=0, aspd=45, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Zeal = Item("Zeal", 1050, Stats(ad=0, ap=0, aspd=18, cs=15, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Rabadons_Deathcap = Item("Rabadon's Deathcap", 3600, Stats(ad=0, ap=120, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Wits_End = Item("Wit's End", 3100, Stats(ad=40, ap=0, aspd=40, cs=0, ah=0, ar=0,
        mr=40, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Rapid_Firecannon = Item("Rapid Firecannon", 2500, Stats(ad=0, ap=0, aspd=35, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Stormrazor = Item("Stormrazor", 2700, Stats(ad=40, ap=0, aspd=15, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Banshees_Veil = Item("Banshee's Veil", 2600, Stats(ad=0, ap=80, aspd=0, cs=0, ah=10, ar=0,
        mr=45, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Aegis_of_the_Legion = Item("Aegis of the Legion", 1400, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=30,
        mr=30, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Redemption = Item("Redemption", 2300, Stats(ad=0, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Fiendish_Codex = Item("Fiendish Codex", 900, Stats(ad=0, ap=35, aspd=0, cs=0, ah=10, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Knights_Vow = Item("Knight's Vow", 2300, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=0,
        mr=0, hp=400, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Frozen_Heart = Item("Frozen Heart", 2500, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=80,
        mr=0, hp=0, mana=400, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Mercurys_Treads = Item("Mercury's Treads", 1100, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=25, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Guardians_Orb = Item("Guardian's Orb", 950, Stats(ad=0, ap=40, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Aether_Wisp = Item("Aether Wisp", 850, Stats(ad=0, ap=30, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Forbidden_Idol = Item("Forbidden Idol", 800, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Rylais_Crystal_Scepter = Item("Rylai's Crystal Scepter", 2600, Stats(ad=0, ap=75, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=400, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Mobility_Boots = Item("Mobility Boots", 1000, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Winters_Approach = Item("Winter's Approach", 2600, Stats(ad=0, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=400, mana=500, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Fimbulwinter = Item("Fimbulwinter", 2600, Stats(ad=0, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=400, mana=860, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Executioners_Calling = Item("Executioner's Calling", 800, Stats(ad=15, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Guinsoos_Rageblade = Item("Guinsoo's Rageblade", 2600, Stats(ad=0, ap=0, aspd=45, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Caulfields_Warhammer = Item("Caulfield's Warhammer", 1100, Stats(ad=25, ap=0, aspd=0, cs=0, ah=10, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Serrated_Dirk = Item("Serrated Dirk", 1100, Stats(ad=30, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Void_Staff = Item("Void Staff", 2800, Stats(ad=0, ap=65, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=45, lethality=0, f_mrp=0, ls=0), legendary=True)
Mercurial_Scimitar = Item("Mercurial Scimitar", 3000, Stats(ad=40, ap=0, aspd=0, cs=20, ah=0, ar=0,
        mr=30, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Quicksilver_Sash = Item("Quicksilver Sash", 1300, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=30, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Youmuus_Ghostblade = Item("Youmuu's Ghostblade", 3000, Stats(ad=55, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=18, f_mrp=0, ls=0), legendary=True)
Randuins_Omen = Item("Randuin's Omen", 2700, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=80,
        mr=0, hp=250, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Hextech_Alternator = Item("Hextech Alternator", 1050, Stats(ad=0, ap=25, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Hextech_Rocketbelt = Item("Hextech Rocketbelt", 3200, Stats(ad=0, ap=90, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=250, mana=0, arp=0, mrp=0, lethality=0, f_mrp=6, ls=0), mythic=True)
Blade_of_The_Ruined_King = Item("Blade of The Ruined King", 3300, Stats(ad=40, ap=0, aspd=25, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=10), legendary=True)
Hexdrinker = Item("Hexdrinker", 1300, Stats(ad=25, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=35, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Maw_of_Malmortius = Item("Maw of Malmortius", 2900, Stats(ad=55, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=50, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Zhonyas_Hourglass = Item("Zhonya's Hourglass", 2600, Stats(ad=0, ap=65, aspd=0, cs=0, ah=10, ar=45,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Ionian_Boots_of_Lucidity = Item("Ionian Boots of Lucidity", 950, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Morellonomicon = Item("Morellonomicon", 2500, Stats(ad=0, ap=80, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=250, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Guardians_Blade = Item("Guardian's Blade", 950, Stats(ad=30, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Umbral_Glaive = Item("Umbral Glaive", 2400, Stats(ad=50, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=10, f_mrp=0, ls=0), legendary=True)
Hullbreaker = Item("Hullbreaker", 2800, Stats(ad=50, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=400, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Guardians_Hammer = Item("Guardian's Hammer", 950, Stats(ad=25, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=10))
Locket_of_the_Iron_Solari = Item("Locket of the Iron Solari", 2500, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=30,
        mr=30, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Seekers_Armguard = Item("Seeker's Armguard", 1000, Stats(ad=0, ap=20, aspd=0, cs=0, ah=0, ar=15,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Gargoyle_Stoneplate = Item("Gargoyle Stoneplate", 3200, Stats(ad=0, ap=0, aspd=0, cs=0, ah=15, ar=60,
        mr=60, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Spectres_Cowl = Item("Spectre's Cowl", 1250, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=25, hp=250, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Mikaels_Blessing = Item("Mikael's Blessing", 2300, Stats(ad=0, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=50, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Scarecrow_Effigy = Item("Scarecrow Effigy", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Stealth_Ward = Item("Stealth Ward", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Farsight_Alteration = Item("Farsight Alteration", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Oracle_Lens = Item("Oracle Lens", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Your_Cut = Item("Your Cut", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Ardent_Censer = Item("Ardent Censer", 2300, Stats(ad=0, ap=60, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Essence_Reaver = Item("Essence Reaver", 2800, Stats(ad=45, ap=0, aspd=0, cs=20, ah=20, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Eye_of_the_Herald = Item("Eye of the Herald", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Kalistas_Black_Spear = Item("Kalista's Black Spear", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Kalistas_Black_Spear = Item("Kalista's Black Spear", 0, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Dead_Mans_Plate = Item("Dead Man's Plate", 2900, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=45,
        mr=0, hp=300, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Titanic_Hydra = Item("Titanic Hydra", 3300, Stats(ad=30, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=500, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Crystalline_Bracer = Item("Crystalline Bracer", 800, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Lost_Chapter = Item("Lost Chapter", 1300, Stats(ad=0, ap=40, aspd=0, cs=0, ah=10, ar=0,
        mr=0, hp=0, mana=300, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Edge_of_Night = Item("Edge of Night", 2900, Stats(ad=50, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=325, mana=0, arp=0, mrp=0, lethality=10, f_mrp=0, ls=0), legendary=True)
Spellthiefs_Edge = Item("Spellthief's Edge", 400, Stats(ad=0, ap=8, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=10, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Frostfang = Item("Frostfang", 400, Stats(ad=0, ap=15, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=70, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Shard_of_True_Ice = Item("Shard of True Ice", 400, Stats(ad=0, ap=40, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=75, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Steel_Shoulderguards = Item("Steel Shoulderguards", 400, Stats(ad=3, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=30, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Runesteel_Spaulders = Item("Runesteel Spaulders", 400, Stats(ad=6, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=100, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Pauldrons_of_Whiterock = Item("Pauldrons of Whiterock", 400, Stats(ad=15, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=250, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Relic_Shield = Item("Relic Shield", 400, Stats(ad=0, ap=5, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=30, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Targons_Buckler = Item("Targon's Buckler", 400, Stats(ad=0, ap=10, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=100, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Bulwark_of_the_Mountain = Item("Bulwark of the Mountain", 400, Stats(ad=0, ap=20, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=250, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Spectral_Sickle = Item("Spectral Sickle", 400, Stats(ad=5, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=10, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Harrowing_Crescent = Item("Harrowing Crescent", 400, Stats(ad=10, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=60, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Black_Mist_Scythe = Item("Black Mist Scythe", 400, Stats(ad=20, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=75, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Oblivion_Orb = Item("Oblivion Orb", 800, Stats(ad=0, ap=30, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Imperial_Mandate = Item("Imperial Mandate", 2500, Stats(ad=0, ap=40, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Force_of_Nature = Item("Force of Nature", 2900, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=70, hp=350, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
The_Golden_Spatula = Item("The Golden Spatula", 7387, Stats(ad=70, ap=120, aspd=50, cs=30, ah=20, ar=30,
        mr=30, hp=250, mana=250, arp=0, mrp=0, lethality=0, f_mrp=0, ls=10))
Horizon_Focus = Item("Horizon Focus", 3000, Stats(ad=0, ap=85, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Cosmic_Drive = Item("Cosmic Drive", 3000, Stats(ad=0, ap=65, aspd=0, cs=0, ah=30, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Blighting_Jewel = Item("Blighting Jewel", 1250, Stats(ad=0, ap=25, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=15, lethality=0, f_mrp=0, ls=0))
Verdant_Barrier = Item("Verdant Barrier", 1000, Stats(ad=0, ap=20, aspd=0, cs=0, ah=0, ar=0,
        mr=25, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Riftmaker = Item("Riftmaker", 3200, Stats(ad=0, ap=80, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=300, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Leeching_Leer = Item("Leeching Leer", 1300, Stats(ad=0, ap=20, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=250, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Night_Harvester = Item("Night Harvester", 3200, Stats(ad=0, ap=90, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=300, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Demonic_Embrace = Item("Demonic Embrace", 3000, Stats(ad=0, ap=60, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=450, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Watchful_Wardstone = Item("Watchful Wardstone", 1100, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Bandleglass_Mirror = Item("Bandleglass Mirror", 950, Stats(ad=0, ap=20, aspd=0, cs=0, ah=10, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Vigilant_Wardstone = Item("Vigilant Wardstone", 1100, Stats(ad=0, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=150, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Crown_of_the_Shattered_Queen = Item("Crown of the Shattered Queen", 2800, Stats(ad=0, ap=60, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=250, mana=600, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Shadowflame = Item("Shadowflame", 3000, Stats(ad=0, ap=100, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Ironspike_Whip = Item("Ironspike Whip", 1100, Stats(ad=30, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Silvermere_Dawn = Item("Silvermere Dawn", 3000, Stats(ad=40, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=35, hp=300, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Deaths_Dance = Item("Death's Dance", 3300, Stats(ad=55, ap=0, aspd=0, cs=0, ah=15, ar=45,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Chempunk_Chainsword = Item("Chempunk Chainsword", 2600, Stats(ad=45, ap=0, aspd=0, cs=0, ah=15, ar=0,
        mr=0, hp=250, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Staff_of_Flowing_Water = Item("Staff of Flowing Water", 2300, Stats(ad=0, ap=50, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Moonstone_Renewer = Item("Moonstone Renewer", 2500, Stats(ad=0, ap=40, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=200, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Goredrinker = Item("Goredrinker", 3300, Stats(ad=55, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=300, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Stridebreaker = Item("Stridebreaker", 3300, Stats(ad=50, ap=0, aspd=20, cs=0, ah=20, ar=0,
        mr=0, hp=300, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Divine_Sunderer = Item("Divine Sunderer", 3300, Stats(ad=40, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=300, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True, passives=[DivineSundererMythic()])
Liandrys_Anguish = Item("Liandry's Anguish", 3200, Stats(ad=0, ap=80, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=0, mana=600, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Ludens_Tempest = Item("Luden's Tempest", 3200, Stats(ad=0, ap=80, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=0, mana=600, arp=0, mrp=0, lethality=0, f_mrp=6, ls=0), mythic=True)
Everfrost = Item("Everfrost", 2800, Stats(ad=0, ap=70, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=250, mana=600, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Bamis_Cinder = Item("Bami's Cinder", 1100, Stats(ad=0, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=300, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Frostfire_Gauntlet = Item("Frostfire Gauntlet", 2800, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=25,
        mr=25, hp=350, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Turbo_Chemtank = Item("Turbo Chemtank", 2800, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=25,
        mr=25, hp=350, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Noonquiver = Item("Noonquiver", 1300, Stats(ad=30, ap=0, aspd=15, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Galeforce = Item("Galeforce", 3400, Stats(ad=60, ap=0, aspd=20, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), mythic=True)
Immortal_Shieldbow = Item("Immortal Shieldbow", 3400, Stats(ad=50, ap=0, aspd=20, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=10), mythic=True, passives=[ImmortalShieldbowMythic()])
Navori_Quickblades = Item("Navori Quickblades", 3400, Stats(ad=60, ap=0, aspd=0, cs=20, ah=30, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
The_Collector = Item("The Collector", 3000, Stats(ad=55, ap=0, aspd=0, cs=20, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=12, f_mrp=0, ls=0), legendary=True)
Rageknife = Item("Rageknife", 800, Stats(ad=0, ap=0, aspd=25, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0))
Duskblade_of_Draktharr = Item("Duskblade of Draktharr", 3100, Stats(ad=60, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=18, f_mrp=0, ls=0), mythic=True)
Eclipse = Item("Eclipse", 3100, Stats(ad=55, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=18, f_mrp=0, ls=0), mythic=True, passives=[EclipseMythic()])
Prowlers_Claw = Item("Prowler's Claw", 3100, Stats(ad=60, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=18, f_mrp=0, ls=0), mythic=True)
Seryldas_Grudge = Item("Serylda's Grudge", 3200, Stats(ad=45, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=0, mana=0, arp=30, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Serpents_Fang = Item("Serpent's Fang", 2600, Stats(ad=55, ap=0, aspd=0, cs=0, ah=0, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=12, f_mrp=0, ls=0), legendary=True)
Axiom_Arc = Item("Axiom Arc", 3000, Stats(ad=55, ap=0, aspd=0, cs=0, ah=25, ar=0,
        mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=10, f_mrp=0, ls=0), legendary=True)
Anathemas_Chains = Item("Anathema's Chains", 2500, Stats(ad=0, ap=0, aspd=0, cs=0, ah=20, ar=0,
        mr=0, hp=650, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
Abyssal_Mask = Item("Abyssal Mask", 2700, Stats(ad=0, ap=0, aspd=0, cs=0, ah=10, ar=0,
        mr=30, hp=450, mana=0, arp=0, mrp=0, lethality=0, f_mrp=0, ls=0), legendary=True)
