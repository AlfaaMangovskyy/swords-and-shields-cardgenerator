import json as j

file = open("warriors.json", "r", encoding = "utf8")
warriors = j.load(file)
file.close()

counter = {
    "Miecz":  0,
    "Luk":    0,
    "Lanca":  0,
    "Woda":   0,
    "Ogien":  0,
    "Ziemia": 0,
    "Wiatr":  0,
}

for warrior_id, warrior_data in warriors.items():
    for class_ in warrior_data["moveset"][0]:
        counter[class_] += 1
    for class_ in warrior_data["moveset"][1]:
        counter[class_] += 1

for class_id, class_count in counter.items():
    print(f"{class_id}: {class_count}")

print(f"\nTotal: {sum(counter.values())}")