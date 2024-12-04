import os

directory = os.fsencode("dataset")
i = 0
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    os.rename("dataset/" + str(filename), "dataset/" + str(i) + ".jpg")
    i += 1
    print(i)