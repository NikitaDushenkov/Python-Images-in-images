import numpy as np
from PIL import Image
import math

def img_from_num(num):
  return Image.open("temporary/" + str(num) + ".jpg")
def mean_color(picture):
  image_array = np.asarray(picture)
  sumr = 0
  sumb = 0
  sumg = 0
  for i in image_array:
    for j in i:
      sumr += j[0]
      sumg += j[1]
      sumb += j[2]
  midr = sumr / (image_array.shape[0] * image_array.shape[1])
  midg = sumb / (image_array.shape[0] * image_array.shape[1])
  midb = sumg / (image_array.shape[0] * image_array.shape[1])
  return (midr, midg, midb)
def dist(color1, color2):
    d = math.sqrt(abs(color1[0]-float(color2[0])**2 + (color1[1]-float(color2[1]))**2 + (color1[2]-float(color2[2]))**2))
    return d

for i in range(12959):
  img3 = img_from_num(i)
  img3 = img3.resize((64, 64), Image.LANCZOS)
  img3.save("temporary/" + str(i) + ".jpg")
  print(i)