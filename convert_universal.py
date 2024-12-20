from PIL import Image
import os

i = 0
directory = os.fsencode("dataset")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    img = Image.open("dataset/" + filename)
    img = img.resize((64, 64), Image.LANCZOS)
    img.save("dataset/" + filename)
    i += 1
    print(i)