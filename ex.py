from PIL import Image
from barcode import EAN8
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
import time
import os


# img = Image.open('barcode.png')
# print('size1 ', img.size)
# # img.show()

# img2 = img.resize((160, 80))
# print('size2 ', img2.size)
# box = (30, 10, 130, 15)
# img3 = img2.crop(box)
# img3.show()
# print('size3 ', img3.size)
# img3.save('1.jpg')


def decode_barcode(img_path):
    img = Image.open(img_path)
    img = img.crop((0, img.size[1] - 5, 102, img.size[1]))
    # print(img.size)
    img.show()
    result = decode(img)
    data = []
    for i in result:
        data.append(i.data.decode("utf-8"))
        print(i.data.decode("utf-8"))
    return data


decode_barcode("output.jpg")
