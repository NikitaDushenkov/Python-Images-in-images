import numpy as np
from PIL import Image
import math
import multiprocessing
import time
from tqdm import tqdm
start_time = time.time()


def img_from_num(num):
    return Image.open("dataset/" + str(num) + ".jpg")

def dist(color1, color2):
    d = math.sqrt((color1[0]-color2[0])**2 + (color1[1]-color2[1])**2 + (color1[2]-color2[2])**2)
    return d


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
    return [midr, midg, midb]


file = open("mid.txt", "r+")
colors = [[float(i.split(" ")[0]), float(i.split(" ")[1]), float(i.split(" ")[2])] for i in file.read().split("\n")]
x = 16777216
length = len(colors)
color_array = []
for i in range(256):
    for j in range(256):
        for h in range(256):
            color_array.append([i, j, h])


def process1(out_array1, from_index, to_index):
    ind = 0
    for i in range(from_index, to_index):
        best = 0
        closest = 100000
        for z in range(length):
            o = dist(colors[z], color_array[i])
            if o < closest:
                closest = o
                best = z
        out_array1[ind] = best
        ind += 1


def process2(out_array2, from_index, to_index):
    ind = 0
    for i in tqdm(range(from_index, to_index)):
        best = 0
        closest = 100000
        for z in range(length):
            o = dist(colors[z], color_array[i])
            if o < closest:
                closest = o
                best = z
        out_array2[ind] = best
        ind += 1


def process3(out_array3, from_index, to_index):
    ind = 0
    for i in range(from_index, to_index):
        best = 0
        closest = 100000
        for z in range(length):
            o = dist(colors[z], color_array[i])
            if o < closest:
                closest = o
                best = z
        out_array3[ind] = best
        ind += 1


def process4(out_array4, from_index, to_index):
    ind = 0
    for i in range(from_index, to_index):
        best = 0
        closest = 100000
        for z in range(length):
            o = dist(colors[z], color_array[i])
            if o < closest:
                closest = o
                best = z
        out_array4[ind] = best
        ind += 1


if __name__ == "__main__":
    out_array1 = multiprocessing.Array('i', x//4)
    out_array2 = multiprocessing.Array('i', x//4)
    out_array3 = multiprocessing.Array('i', x//4)
    out_array4 = multiprocessing.Array('i', x // 4 + x % 4)
    p1 = multiprocessing.Process(target=process1, args=(out_array1, 0, x//4))
    p2 = multiprocessing.Process(target=process2, args=(out_array2, x//4, x//4*2))
    p3 = multiprocessing.Process(target=process3, args=(out_array3, x//4*2, x//4*3))
    p4 = multiprocessing.Process(target=process4, args=(out_array4, x//4*3, x))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    out = out_array1[:] + out_array2[:] + out_array3[:] + out_array4[:]
    f = open("mid2.txt", "r+")
    for i in range(x):
        f.write(str(out[i]) + "\n")
    print("--- %s seconds ---" % (time.time() - start_time))
