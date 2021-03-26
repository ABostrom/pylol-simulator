

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

class Stats:
    def __init__(self, ad, ap, as, cs, csd, ar, mr, hp) -> None:
        self.ad = ad
        self.ap = ap
        self.as = as
        self.cs = cs
        self.csd = csd
        self.ar = ar
        self.mr = mr
        self.hp = hp

class ChampionBaseStats(Stats):

    def __init__(self, ad, ap, as, cs, csd, ar, mr, hp,
                ad_growth, ap_growth, as_growth, ar_growth, mr_growth, hp_growth) -> None:

        super.__init__(ad, ap, as, cs, csd, ar, mr, hp)

        # statistics that govern a champions growth
        self.ad_growth= ad_growth
        self.ap_growth = ap_growth
        self.as_growth = as_growth
        self.ar_growth = ar_growth
        self.mr_growth = mr_growth
        self.hp_growth = hp_growth

        #TODO: might need to represent champion level.

