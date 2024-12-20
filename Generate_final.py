import numpy as np
from PIL import Image
import multiprocessing
import time
from tqdm import tqdm


start_time = time.time()
#settings
size = 4
img_num = 19
thread_count = 6

Image.MAX_IMAGE_PIXELS = None


def process(from_index, to_index, num, old_length, out_, size_y):
    length = (to_index-from_index)
    img_ = Image.new('RGB', (length * 64,size_y * 64))
    if from_index == 0:
        for i in tqdm(range(length * size_y)):
            temp_ = Image.open("dataset/" + str(out_[i // length][i % length]) + ".jpg")
            img_.paste(temp_, (i % length * 64, i // length * 64))
    else:
        for i in range((to_index-from_index) * size_y):
            temp_ = Image.open("dataset/" + str(out_[i // length][i % length + old_length * num]) + ".jpg")
            img_.paste(temp_, (i % (to_index-from_index) * 64, i // (to_index-from_index) * 64))
    img_.save("Images/between_process" + str(num) + ".jpg")



if __name__ == "__main__":
    file = open("mid2.txt", "r+")
    mid2 = file.read().split("\n")
    color_array = [[[0 for i in range(256)] for j in range(256)] for h in range(256)]
    o = 0
    for x in range(256):
        for y in range(256):
            for z in range(256):
                color_array[x][y][z] = int(mid2[o])
                o += 1
    img = Image.open("Images/test_image_" + str(img_num) + ".jpg")
    image_array = np.asarray(img)
    img = img.resize((len(image_array[0]) // size, len(image_array) // size), Image.LANCZOS)
    image_array = np.asarray(img)
    x = len(image_array) * len(image_array[0])
    size_x = len(image_array[0])
    size_y = len(image_array)

    result = []
    for i in tqdm(range(x)):
        cur = image_array[i // size_x][i % size_x]
        result.append(color_array[int(cur[0])][int(cur[1])][int(cur[2])])
    out_better = []
    for i in range(size_y):
        out_better.append(result[i * size_x:(i + 1) * size_x])

    print("image x image:", len(image_array[0]), len(image_array))  # вставляемые картинки 64 X 64
    #stitch
    print("stiching...")

    procceses = []
    for i in range(thread_count - 1):
        procceses.append(multiprocessing.Process(target=process, args=(
                    size_x // thread_count * i,
                    size_x // thread_count * (i + 1), i, size_x // thread_count, out_better, size_y)))
    procceses.append(multiprocessing.Process(target=process, args=(
                    size_x // thread_count * (thread_count - 1), size_x, thread_count-1, size_x // thread_count, out_better, size_y)))

    for i in range(thread_count):
        procceses[i].start()
        print("started:", i, "at", time.time() - start_time)
    for i in range(thread_count):
        procceses[i].join()

    img = Image.new('RGB', (len(image_array[0]) * 64, len(image_array) * 64))
    for i in range(thread_count):
        temp = Image.open("Images/between_process" + str(i) + ".jpg")
        img.paste(temp, (i*(size_x // thread_count) * 64, 0))
    img.save("Images/test_image_"+str(img_num)+"_redo.jpg")
    print("--- %s seconds ---" % (time.time() - start_time))