import json


# remaps the external stat names to the internal naming conventions.
def extract_stats(stats, name):
    # Create a dict for champions which exist with an attack speed ratio which isn't explicitly defined in the JSON.
    as_ratio_dict = {"Akshan": 0.400, "Amumu": 0.638, "Caitlyn": 0.568, "DrMundo": 0.625, "Ekko": 0.625,
                     "Gangplank": 0.690, "Gragas": 0.625, "Graves": 0.490, "Kayle": 0.667, "Kennen": 0.690,
                     "Lissandra": 0.625, "Lux": 0.625, "Malphite": 0.638, "Maokai": 0.695, "Nautilus": 0.612,
                     "Neeko": 0.670, "Nocturne": 0.668, "Qiyana": 0.625, "Rammus": 0.625, "Sejuani": 0.625,
                     "Senna": 0.300, "Seraphine": 0.625, "Shen": 0.651, "Tristana": 0.679, "Vex": 0.625,
                     "Volibear": 0.700, "MonkeyKing": 0.658, "Yasuo": 0.670, "Zac": 0.638, "Zeri": 0.568}
    # set stats to 0 by default so we can handle errors in future (ie no mana)
    hp = stats.get("hp", 0)
    hp_growth = stats.get("hpperlevel", 0)
    mana = stats.get("mp", 0)
    mana_growth = stats.get("mpperlevel", 0)
    ar = stats.get("armor", 0)
    ar_growth = stats.get("armorperlevel", 0)
    mr = stats.get("spellblock", 0)
    mr_growth = stats.get("spellblockperlevel", 0)
    ad = stats.get("attackdamage", 0)
    ad_growth = stats.get("attackdamageperlevel", 0)
    aspd_growth = stats.get("attackspeedperlevel", 0)
    base_aspd = stats.get("attackspeed", 0)
    as_ratio = as_ratio_dict.get(name, 0)
    return hp, hp_growth, mana, mana_growth, ar, ar_growth, mr, mr_growth, ad, ad_growth, aspd_growth, base_aspd, as_ratio


def main():
    # read the json file
    championFile = open("./data/champion.json", "r", encoding="utf-8")
    data = json.load(championFile)
    data = data.get("data")
    out = open("./out.champ", "w")
    # Loop through every champion in the data.
    for name in data:
        # Get the champion-specific data from the JSON data.
        championData = data.get(name)
        # Get the stats of the champion.
        championStats = championData.get("stats")
        # Extract the internal named stats from the JSON names.
        hp, hp_growth, mana, mana_growth, ar, ar_growth, mr, mr_growth, ad, ad_growth, aspd_growth, base_aspd, as_ratio = extract_stats(
            championStats, name)
        # Print the data and write it to the file 'out.champ'.
        line = (
            f"""{name} = partial(Champion, name=\"{name}\", ad={ad}, ad_growth={ad_growth}, hp={hp}, hp_growth={hp_growth}, ar={ar}, ar_growth={ar_growth}, mr={mr}, 
            mr_growth={mr_growth}, base_aspd={base_aspd}, aspd_growth={aspd_growth}, as_ratio={as_ratio}, mana={mana}, mana_growth={mana_growth})""")
        print(line)
        out.write(line + "\n")
    out.close()
    # obtain a champion based on their name
    pass


if __name__ == '__main__':
    main()
