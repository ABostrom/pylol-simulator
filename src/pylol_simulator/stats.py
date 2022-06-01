'''
This is an object to represent a bundle of stats that a champion may possess.

offensive stats:
Attack Damage           (ad)
Ability Power           (ap)
Attack Speed            (as)
Critical Strike Chance  (cs)
Critical Strike Damage  (csd)
Ability Haste           (ah)

Armour Penetration      (arp)
Magic Penetration       (mrp)
Lethality               (lethality)
Flat Magic Penetration  (f_mrp)

defensive stats:    
Armour                  (ar)
Magic Resistance        (mr)   
Health                  (hp)
'''


class Stats(object):
    def __init__(self, ad=0, ap=0, aspd=0, ah=0, cs=0, csd=0, ar=0, mr=0, hp=0, mana=0, arp=0, mrp=0, lethality=0,
                 f_mrp=0, ls=0) -> None:
        self.ad = ad
        self.ap = ap
        self.aspd = aspd
        self.cs = cs if cs < 1 else cs/100 #if the cs is greater than 1 we scale it to be between 0 and 1
        self.csd = csd
        self.ah = ah
        self.ar = ar
        self.mr = mr
        self.hp = hp
        self.mana = mana
        self.arp = arp
        self.mrp = mrp
        self.lethality = lethality
        self.f_mrp = f_mrp
        self.ls = ls

    def __str__(self) -> str:
        return f"AD   {self.ad}\tAP {self.ap}\nAR   {self.ar}\tMR {self.mr}\nASPD {self.aspd}\tAH {self.ah}\n"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other):
        return Stats(ad=self.ad + other.ad, ap=self.ap + other.ap,
                     aspd=self.aspd + other.aspd, ah=self.ah + other.ah, cs=self.cs + other.cs,
                     csd=self.csd + other.csd, ar=self.ar + other.ar, mr=self.mr + other.mr, hp=self.hp + other.hp,
                     mana=self.mana + other.mana, ls=self.ls + other.ls,
                     lethality=self.lethality + other.lethality, f_mrp=self.f_mrp + other.f_mrp,
                     arp=stack_mutiplicative(self.arp, other.arp), mrp=stack_mutiplicative(self.mrp, other.mrp))


def stack_mutiplicative(pen1, pen2):
    return (1 - ((1 - (pen1 / 100)) * (1 - (pen2 / 100)))) * 100
