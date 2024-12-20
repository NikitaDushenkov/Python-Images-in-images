from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()
i = 0
directory = os.fsencode("dataset")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    img = Image.open("dataset/" + filename)
    img = img.convert('RGB')
    name = filename.split(".")[0]
    img.save("dataset/" + name + ".jpg")
    i += 1
    print(i)