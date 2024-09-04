import json as j

result = {}

input_data = j.load(open("warriors.json", "r", encoding = "utf8"))

n_miecz  = 0
n_luk    = 0
n_lanca  = 0
n_woda   = 0
n_ogien  = 0
n_ziemia = 0
n_wiatr  = 0

for warrior_name, warrior_data in input_data.items():
    # warrior_name #
    for block in warrior_data["moveset"]:
        for move_class in block:
            match move_class:
                case "Miecz"  : n_miecz   += 1 * warrior_data["cards"]
                case "Luk"    : n_luk     += 1 * warrior_data["cards"]
                case "Lanca"  : n_lanca   += 1 * warrior_data["cards"]
                case "Woda"   : n_woda    += 1 * warrior_data["cards"]
                case "Ogien"  : n_ogien   += 1 * warrior_data["cards"]
                case "Ziemia" : n_ziemia  += 1 * warrior_data["cards"]
                case "Wiatr"  : n_wiatr   += 1 * warrior_data["cards"]
                case _: pass

print(f"Miecz    :  {n_miecz}")
print(f"Luk      :  {n_luk}")
print(f"Lanca    :  {n_lanca}")
print(f"Woda     :  {n_woda}")
print(f"Ogien    :  {n_ogien}")
print(f"Ziemia   :  {n_ziemia}")
print(f"Wiatr    :  {n_wiatr}")