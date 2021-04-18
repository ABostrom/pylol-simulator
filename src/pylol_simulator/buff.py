from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .summoner import Summoner


from .damage import Damage

# this will be a class to apply a buff to a Summoner
# regular buffs will be permanent


class Buff:

    def __init__(self, name: str, duration: float, consumes_on_atk = False) -> None:
        self.name = name
        self.permanent = duration == None
        self.duration = duration if not self.permanent else 0
        self.duration_remaining = self.duration
        self.expired = False
        self.consumes_on_atk = consumes_on_atk

    # need to be able to tick.
    def update(self, delta_time: float):
        # don't need ticking behaviour if permanent.
        if self.permanent:
            return

        self.duration_remaining -= delta_time

        if self.duration_remaining <= 0:
            self.expired = True

    # need some function to refresh/reset buffs
    def refresh(self):
        self.duration_remaining = self.duration

    # is this buff consumed on basic attacking.
    def consumes_on_attack(self) -> bool:
        return self.consumes_on_atk

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        pass

    # TODO: is this buff consumed on abilities

    # check buffs are equal
    def __eq__(self, o: Buff) -> bool:
        return self.name == o.name

    def __hash__(self) -> int:
        return hash(self.name)


# consider how internal CD might work for Sheen items.
class SheenSpellBlade(Buff):
    def __init__(self) -> None:
        super().__init__("Spell Blade", duration=10.0, consumes_on_atk=True)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        #100% of base ad
        return Damage(physical_damage=attacker.base_ad)


class TriforceSpellBlade(Buff):
    def __init__(self) -> None:
        super().__init__("Spell Blade", duration=10.0, consumes_on_atk=True)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        # 200% of base ad
        return Damage(physical_damage=attacker.base_ad * 2)


class LichBaneSpellBlade(Buff):
    def __init__(self) -> None:
        super().__init__("Spell Blade", duration=10.0, consumes_on_atk=True)

    def on_basic_attack(self, attacker: Summoner, defender: Summoner):
        # 150% of base ad + 40% of AP
        return Damage(physical_damage=attacker.base_ad * 1.5, magic_damage=attacker.ap * 0.4)
