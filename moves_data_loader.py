CATEGORY = "Miecz"

RECRUITMENT_LEVELS = {
    "I"   : 1,
    "II"  : 2,
    "III" : 3,
    "IV"  : 4,
    "V"   : 5,
}

file = open("moves_data.csv", "r")
raw = [n.removesuffix("\n") for n in file.readlines()[1:]]
file.close()

result = []

for line in raw:
    move_data = {}
    raw_data = line.split(",")

    if raw_data[0] == "": continue
    if raw_data[2] != CATEGORY: continue

    rng = 0 - 1
    for i in raw_data[4:6+1]:
        if i == "1": rng += 1

    move_data["name"]   = raw_data[1]
    move_data["dmg"]    = raw_data[3]
    move_data["range"]  = rng
    move_data["level"]  = RECRUITMENT_LEVELS[raw_data[0]]
    move_data["desc"]   = raw_data[7].replace("\"")
    move_data["mech"]   = raw_data[8].replace("\"")

    result.append(move_data)