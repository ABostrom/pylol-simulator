

'''
This is an object to represent a bundle of stats that a champion may possess.

offensive stats:
Attack Damage           (ad)
Ability Power           (ap)
Attack Speed            (as)
Critical Strike Chance  (cs)
Critical Strike Damage  (csd)

defensive stats:    
Armour                  (ar)
Magic Resistance        (mr)   
Health                  (hp)
'''

class Stats(object):
    def __init__(self, ad=0, ap=0, aspd=0, cs=0, csd=0, ar=0, mr=0, hp=0) -> None:
        self.ad = ad
        self.ap = ap
        self.aspd = aspd
        self.cs = cs
        self.csd = csd
        self.ar = ar
        self.mr = mr
        self.hp = hp

class ChampionBaseStats(Stats):

    def __init__(self, ad=0, ap=0, aspd=0, cs=0, csd=0, ar=0, mr=0, hp=0,
                ad_growth=0, ap_growth=0, aspd_growth=0, ar_growth=0, mr_growth=0, hp_growth=0) -> None:

        super().__init__(ad, ap, aspd, cs, csd, ar, mr, hp)

        # statistics that govern a champions growth
        self.ad_growth= ad_growth
        self.ap_growth = ap_growth
        self.aspd_growth = aspd_growth
        self.ar_growth = ar_growth
        self.mr_growth = mr_growth
        self.hp_growth = hp_growth

        #TODO: might need to represent champion level.



def growth_formula(base, growth, level):
    return base + growth * (level-1) * (0.7025 + 0.0175 * (level-1))