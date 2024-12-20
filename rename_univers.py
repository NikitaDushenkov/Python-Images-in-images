import os

directory = os.fsencode("dataset")
i = 0
for file in os.listdir(directory):
    filename = os.fsdecode(file).lower()
    ext = filename.split(".")[1]
    os.rename("dataset/" + str(filename), "dataset/" + str(i) + "." + ext)
    i += 1
    print(i)