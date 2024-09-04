import math
import os
from PIL import Image, ImageOps, ImageDraw, ImageFont
import json as j

font_header = ImageFont.truetype("font.ttf", 35)
font_subheader = ImageFont.truetype("font.ttf", 25)
font_description = ImageFont.truetype("font.ttf", 15)
font_ability = ImageFont.truetype("font.ttf", 25)

def get_move(cls_ : str, id_ : int):
    result = moves[cls_][id_].copy()
    result["class"] = cls_
    return result

ABILITIES = j.load(open(f"abilities.json", f"r", encoding = f"utf8"))

def make_card(warrior_data : dict, warrior_id : str) -> None:
    result_card = Image.open(f"data/card.png")

    result_card.paste(Image.open(f"card_drawings/{warrior_id}.png").resize((607 + 2, 316 + 2)), (6, 70))

    painter = ImageDraw.Draw(result_card)
    painter.text((10, 10), asciinate(warrior_data["name"]), (255, 255, 255), font = font_header)

    ability_name = ABILITIES[warrior_data["ability"]]["name"] if warrior_data["ability"] else "-" #str(warrior_data["ability"])#
    painter.text((170, 400), asciinate(ability_name), (255, 0, 0), font = font_subheader)

    if ability_name != "-":
        ability_description = ABILITIES[warrior_data["ability"]]["desc"]
        n = 0
        for line in ability_description.split("\n"):
            painter.text((25, 450 + 30 * n), asciinate(line), (255, 255, 255), font = font_ability)
            n += 1

    vertical = 0
    horizontal = 0
    for i in range(warrior_data["hp"]):
        result_card.paste(Image.open("data/health_point.png"), (result_card.width - 40 - horizontal * 40, 10 + 15 * vertical))
        horizontal += 1
        if horizontal == 4:
            horizontal = 0
            vertical += 1

    row = 0
    for move_data in warrior_data["moveset"]:
        if isinstance(move_data, list):
            n = 0
            all_icons_width = len(move_data) * 64 + (len(move_data) - 1) * 10
            for moveclass in move_data:
                icon_x_offset = n * 64 + (n - 1) * 10
                icon_x = round(result_card.width / 2 - all_icons_width / 2 + icon_x_offset)

                icon_y = 700 + 77 * row + 38 - 32

                img = Image.open(f"data/moveclass_{moveclass}_64.png")
                result_card.paste(img, (icon_x, icon_y))
                n += 1

        elif isinstance(move_data, dict):
            pass

        row += 1

    result_card.save(f"cards/{warrior_id}.png")

def asciinate(text : str):
    return text.replace(
        "ą", "a"
    ).replace(
        "ę", "e"
    ).replace(
        "ó", "o"
    ).replace(
        "ż", "z"
    ).replace(
        "ź", "z"
    ).replace(
        "ł", "l"
    ).replace(
        "ś", "s"
    ).replace(
        "ń", "n"
    ).replace(
        "Ż", "Z"
    ).replace(
        " ", "  "
    ).replace(
        "Ł", "L"
    ).replace(
        "ć", "c"
    )

def make_move_card(move_data : dict) -> None:
    result_card = Image.open(f"data/move_card.png")

    painter = ImageDraw.Draw(result_card)
    painter.text((25, 30), asciinate(move_data["name"]), (255, 255, 255), font = font_header)

    img = Image.open(f"data/moveclass_{move_data['class']}_64.png")
    result_card.paste(
        img,
        (
            620 - 10 - img.width, # 100 - 10 - img.height #
            round(100 / 2 - img.height / 2),
        ),
    )

    n = 0
    for line in move_data["desc"].split("\n"):
        print(asciinate(line))
        painter.text((25, 420 + 30 * n), asciinate(line), (235, 235, 235), font = font_subheader)
        n += 1

    for xo in range(move_data["dmg"] + 1):
        img = Image.open(f"data/damage.png")

        result_card.paste(
            img,
            (
                620 - (10 + img.width) * xo,
                777 + round(100 / 2 - img.height / 2),
            ),
        )

    painter.text((25, 777 + 30), move_data["name"], (255, 255, 255), font = font_header)

    result_card.save(f"move_cards/{move_data['name'].lower().replace(' ', '_')}.png")

def create_print_page(card_ids : list[str]):
    result_page = Image.new("RGBA", (2480, 3508), (255, 255, 255, 255))
    offset_x = 0
    offset_y = 0
    for card_id in card_ids:
        card_img = Image.open(f"cards/{card_id}.png")
        card_img = card_img.resize((math.floor(2480 / 3) - 40, math.floor(3508 / 3) - 40))
        result_page.paste(card_img, (45 + offset_x * card_img.width + offset_x * 5, 45 + offset_y * card_img.height + offset_y * 5))

        offset_x += 1
        if offset_x == 3:
            offset_x = 0
            offset_y += 1

    result_page.save(f"pages/{len(os.listdir('pages'))}_awers.png")



    result_page = Image.new("RGBA", (2480, 3508), (255, 255, 255, 255))
    offset_x = 0
    offset_y = 0
    for card_id in card_ids:
        card_img = Image.open(f"data/warrior_reverse_{warriors[card_id]['recruit']}.png")
        card_img = card_img.resize((math.floor(2480 / 3) - 30, math.floor(3508 / 3) - 30))
        result_page.paste(card_img, (45 + (2 - offset_x) * card_img.width, 45 + offset_y * card_img.height))

        offset_x += 1
        if offset_x == 3:
            offset_x = 0
            offset_y += 1

    result_page.save(f"pages/{len(os.listdir('pages')) - 1}_rewers.png")

def make_print_pages():
    pages = []
    current_page = []
    n = 0
    for warrior_id, warrior in warriors.items():
        # warrior_id #
        for i in range(warrior["cards"]):
            current_page.append(warrior_id)
            n += 1

            if n == 9:
                pages.append(current_page)
                current_page = []
                n = 0

    return pages

warriors = j.load(open("warriors.json", "r", encoding="utf8"))
moves = j.load(open("moves.json", "r", encoding="utf8"))
# make_card(warriors["rycerz_1"], "rycerz_1")
# make_card(warriors["rycerz_2"], "rycerz_2")
# make_card(warriors["husarz"], "husarz")
# make_move_card(get_move("blade", 0))
# make_move_card(get_move("blade", 1))
# create_print_page([
#     "rycerz_1",
#     "rycerz_1",
#     "rycerz_1",
#     "rycerz_1",
#     "rycerz_2",
#     "rycerz_2",
#     "rycerz_2",
#     "husarz",
#     "husarz",
# ])

for warrior_id in warriors.keys():
    # if not f"{warrior_id}.png" in os.listdir(f"cards/"):
        make_card(warriors[warrior_id], warrior_id)

for page in make_print_pages():
    create_print_page(page)

# create_print_page(["husarz", "mag_wody"]) #