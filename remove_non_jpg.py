import os

directory = os.fsencode("dataset")

for file in os.listdir(directory):
    filename = os.fsdecode(file).lower()
    ext = filename.split(".")[1]
    if ext.lower() != "jpg":
        os.remove("dataset/" + filename)
        print(ext)