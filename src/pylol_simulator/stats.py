'''
This is an object to represent a bundle of stats that a champion may possess.

offensive stats:
Attack Damage           (ad)
Ability Power           (ap)
Attack Speed            (as)
Critical Strike Chance  (cs)
Critical Strike Damage  (csd)
Ability Haste           (ah)

defensive stats:    
Armour                  (ar)
Magic Resistance        (mr)   
Health                  (hp)
'''


class Stats(object):
    def __init__(self, ad=0, ap=0, aspd=0, ah=0, cs=0, csd=0, ar=0, mr=0, hp=0) -> None:
        self.ad = ad
        self.ap = ap
        self.aspd = aspd
        self.cs = cs
        self.csd = csd
        self.ah = ah
        self.ar = ar
        self.mr = mr
        self.hp = hp

    def __str__(self) -> str:
        return f"AD {self.ad}\tAP {self.ap}\nAR {self.ar}\tMR {self.mr}\nASPD {self.aspd}\tAH {self.ah}\n"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other):
        return Stats(ad=self.ad+other.ad, ap=self.ap+other.ap,
                     aspd=self.aspd+other.aspd, ah=self.ah+other.ah, cs=self.cs+other.cs,
                     csd=self.csd+other.csd, ar=self.ar+other.ar, mr=self.mr+other.mr, hp=self.hp+other.hp)
