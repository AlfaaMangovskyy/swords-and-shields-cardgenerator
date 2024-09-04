from PIL import Image
import os

for imagepath in os.listdir("cards"):
    img = Image.open(f"cards/{imagepath}")
    img = img.crop((6, 70, 613, 386))
    img.save(f"card_drawings/{imagepath}")