import os
from PIL import Image
import numpy as np

directory = os.fsencode("dataset")
i = 0
count2 = 0
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    img = Image.open("dataset/"+filename)
    imgarr = np.asarray(img)
    count = 0
    try:
        for i in range(len(imgarr[0])):
            if imgarr[0][i][0] < 10 and imgarr[0][i][1] < 10 and imgarr[0][i][2] <10:
                count +=1
    except:
        pass
    if count >= 60:
        count2 +=1
        os.remove("dataset/"+filename)
print(count2)