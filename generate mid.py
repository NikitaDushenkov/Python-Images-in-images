import numpy as np
from PIL import Image
def mean_color(picture):
  image_array = np.asarray(picture)
  sumr = 0
  sumg = 0
  sumb = 0
  try:
    for i in image_array:
      for j in i:
        sumr += j[0]
        sumg += j[1]
        sumb += j[2]
    midr = sumr / (image_array.shape[0] * image_array.shape[1])
    midg = sumg / (image_array.shape[0] * image_array.shape[1])
    midb = sumb / (image_array.shape[0] * image_array.shape[1])
  except:
    midr = 1000
    midg = 1000
    midb = 1000
  return (midr, midg, midb)
def img_from_num(num):
  return Image.open("dataset/" + str(num) + ".jpg")

f = open("mid.txt", "r+")

for i in range(12760):
    mid = mean_color(img_from_num(i))
    f.write(str(mid[0]) + " " + str(mid[1]) + " " + str(mid[2]) + "\n")
    print(i)