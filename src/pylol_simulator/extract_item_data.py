import json
import re

from bs4 import BeautifulSoup

from ScrapeData import scrape_legendary_items_from_wiki, scrape_mythic_items_from_wiki


# remaps the external stat names to the internal naming conventions.
def extract_stats(stats):
    # The stats in this function are defaulted to 0 if they are not found within the external data.
    cost = stats.get("cost", 0)
    ad = stats.get("flat_attack_damage", 0)
    ap = stats.get("flat_ability_power", 0)
    aspd = stats.get("attack_speed", 0)
    cs = stats.get("critical_strike_chance", 0)
    ah = stats.get("flat_ability_haste", 0)
    ar = stats.get("flat_armor", 0)
    mr = stats.get("flat_magic_resist", 0)
    hp = stats.get("flat_health", 0)
    mana = stats.get("flat_mana", 0)
    arp = stats.get("armor_penetration", 0)
    mrp = stats.get("magic_penetration", 0)
    lethality = stats.get("flat_lethality", 0)
    f_mrp = stats.get("flat_magic_penetration", 0)
    ls = stats.get("life_steal", 0)
    return cost, ad, ap, aspd, cs, ah, ar, mr, hp, mana, arp, mrp, lethality, f_mrp, ls


# Check if the given name is in the list of item names.
# This function returns the 'proper' item name to remove it from future searches to optimise performance.
def is_found_in_list_of_item_names(name, items):
    n = re.sub(" ", "_", re.sub("[^0-9A-Za-z ]", "", name.upper()))
    # print(f"Testing {name}/{n} for legendary status: ", end='')
    for item in items:
        i = re.sub(" ", "_", re.sub("[^0-9A-Za-z ]", "", item.upper()))
        # print(i, n, f"Result: {i == n}")
        if i == n:
            # print("True")
            return True, item
    # print("False")
    return False, None


def main():
    # Get all legendary items.
    legendary_items = scrape_legendary_items_from_wiki()
    print(f"Found {len(legendary_items)} legendary items on the Wiki.")
    # Get all mythic items.
    mythic_items = scrape_mythic_items_from_wiki()
    print(f"Found {len(mythic_items)} mythic items on the Wiki.")
    # this is a list of all of the currently coded items with their passives
    blackList = ["Recurve Bow", "Kraken Slayer", "Lord Dominik's Regards", "Sheen", "Trinity Force", "Lich Bane",
                 "Nashor's Tooth"]
    # read the json file
    itemFile = open("./data/item.json", "r", encoding="utf-8")
    data = json.load(itemFile)
    data = data.get("data")
    out = open("./out.item", "w")
    # placeholders for debugging purposes.
    mythics, legends = 0, 0
    # Loop through every item.
    for name in data:
        # Get the items name.
        itemData = data.get(name)
        itemName = itemData.get("name")
        # Create a formatted name, used for the Python-compatible variable names.
        formatted_itemName = re.sub(" ", "_", re.sub("[^0-9A-Za-z ]", "", itemName).strip())
        # Check if the item has already been added elsewhere.
        if itemName in blackList:
            continue
        # Get the gold data for the 'cost' attribute.
        itemGold = itemData.get("gold")
        # Get the description value, parsed to obtain the stats.
        itemDescription = itemData.get("description")
        # Determine if the item is mythic or not.
        is_mythic, mythic_name = is_found_in_list_of_item_names(itemName, mythic_items)
        # Determine if the item is legendary or not.
        is_legendary, legendary_name = is_found_in_list_of_item_names(itemName, legendary_items)
        # Parse the description with BeautifulSoup4.
        parser = BeautifulSoup(itemDescription, features='html.parser')
        regex = re.compile("<attention>[0-9]+[%]?</attention> [\\w ]+<")
        parsed = parser.find('maintext')
        if parsed is None:
            # MainText isn't found in placeholder items, skip them.
            continue
        stats = str(parsed.findChildren()[0])
        entries = regex.findall(stats)
        stats = {
            "cost": itemGold.get("total")
        }
        # Loop through each entry found in the description
        for entry in entries:
            entry = re.sub("[^0-9a-zA-Z% ]", "", entry)
            entry = entry.replace("attention", "")
            details = entry.split(" ")
            # Determine the name for the stat
            stat_name = "_".join(details[1:]).lower()
            # Determine the value for the stat
            if "%" not in details[0]:
                stats["flat_" + stat_name] = int(details[0])
            else:
                stat_value = details[0]
                stat_value = int(stat_value.replace("%", ""))
                stats[stat_name] = stat_value

        # Extract the stats from the filtered description data.
        cost, ad, ap, aspd, cs, ah, ar, mr, hp, mana, arp, mrp, lethality, f_mrp, ls = extract_stats(stats)

        # Print the data and also write it to the file.
        line = (
            f"""{formatted_itemName} = Item(\"{itemName}\", {cost}, Stats(ad={ad}, ap={ap}, aspd={aspd}, cs={cs}, ah={ah}, ar={ar}, 
        mr={mr}, hp={hp}, mana={mana}, arp={arp}, mrp={mrp}, lethality={lethality}, f_mrp={f_mrp}, ls={ls})""")
        print(line, end='')
        if is_mythic:
            print(", mythic=True", end='')
            mythics += 1
            mythic_items.remove(mythic_name)
        if is_legendary:
            print(", legendary=True", end='')
            legends += 1
            legendary_items.remove(legendary_name)
        print(")")
        out.write(line + (", mythic=True" if is_mythic else "") + (", legendary=True" if is_legendary else "") + ")\n")
    print(f"\nLoaded {len(data)} items, {mythics} of which are mythical and {legends} are legendary.")
    out.close()
    pass


if __name__ == '__main__':
    main()
