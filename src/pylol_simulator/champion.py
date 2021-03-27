
from .stats import Stats

from functools import partial


class Champion:

    def __init__(self, name, level=1, ad=0, ap=0, aspd=0, cs=0, csd=175, ar=0, mr=0, hp=0,
                 ad_growth=0, ap_growth=0, aspd_growth=0, ar_growth=0, mr_growth=0, hp_growth=0) -> None:

        self.base_stats = Stats(ad=ad, ap=ap, aspd=aspd,
                                cs=cs, csd=csd, ar=ar, mr=mr, hp=hp)
        self.ad_growth = ad_growth
        self.ap_growth = ap_growth
        self.aspd_growth = aspd_growth
        self.ar_growth = ar_growth
        self.mr_growth = mr_growth
        self.hp_growth = hp_growth

        self.name = name
        self.level = level
        self.generate_bonus_stats(level)


    def generate_bonus_stats(self, level):
        # simplify function call.
        f = partial(growth_formula, level)
        self.bonus_stats = Stats(ad=f(self.ad_growth), ap=f(self.ap_growth), aspd=f(self.aspd_growth),
                                 ar=f(self.ar_growth), mr=f(self.mr_growth), hp=f(self.hp_growth))

        self.current_stats = self.base_stats + self.bonus_stats

    def level_up(self):
        if self.level < 18:
            self.level += 1
            self.generate_bonus_stats(self.level)

    def get_ad(self):
        return self.current_stats.ad

    def get_base_aspd(self):
        return self.base_stats.aspd

    def get_bonus_aspd(self):
        return self.bonus_stats.aspd

    def get_ap(self):
        return self.current_stats.ap

    def get_ar(self):
        return self.current_stats.ar

    def get_mr(self):
        return self.current_stats.mr

    def get_hp(self):
        return self.current_stats.hp


def growth_formula(level, growth):
    return growth * (level-1) * (0.7025 + 0.0175 * (level-1))


from functools import partial

# create a partial function from the champion 
Aatrox = partial(Champion,name="Aatrox", ad=60, ad_growth=5, hp=580, hp_growth=90, ar=38,
                  ar_growth=3.25, mr=32, mr_growth=1.25, aspd=0.651, aspd_growth=2.5)
