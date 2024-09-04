import json as j

RECRUITMENT_LEVELS = {
    "I"   : 1,
    "II"  : 2,
    "III" : 3,
    "IV"  : 4,
    "V"   : 5,
}

def count(dictionary : dict, key : str):
    n = 0
    for k, v in dictionary.items():
        if key.startswith(k): n += 1

    return n

with open("warriors_data.csv", encoding = "utf8") as file:
    result = {}
    for line in file.readlines()[1:]:
        insert = line.removesuffix("\n").split(",")
        warrior = {}

        warrior["cards"]    = int(insert[0])
        warrior["name"]     = insert[1]
        warrior["recruit"]  = RECRUITMENT_LEVELS[insert[2]]
        warrior["hp"]       = int(insert[3])
        warrior["ability"]  = insert[4].lower().replace(" ", "_")
        warrior["moveset"]  = []

        warrior["moveset"].append(insert[5].split(" | "))
        warrior["moveset"].append(insert[6].split(" | "))

        warrior_id = warrior["name"].lower().replace(" ", "_")
        if warrior_id in result.keys():
            # warrior_id += f"_{count(result, warrior_id)}" #
            warrior_id += f"_{warrior['recruit']}"

        if warrior_id in result.keys():
            warrior_id += f"_{count(result, warrior_id)}"

        result[warrior_id] = warrior

    print(result)