from PIL import Image
from barcode import EAN8
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode

NUMBERS = "1114567"
INPUT_IMG = "input.jpg"
OUTPUT_NAME = "output.jpg"
COLOR = "red-black"  # OPTIONS: 'grey-red', 'yellow', red-black'


def decode_barcode(img_path):
    img = Image.open(img_path)
    result = decode(img)
    data = []
    for i in result:
        data.append(i.data.decode("utf-8"))
        # print(i.data.decode('utf-8'))
    return data


def change_color(img_path, option=None):

    img = Image.open(img_path)
    img = img.convert("RGB")

    datas = img.getdata()

    new_image_data = []

    if option == "grey-red":
        replace_white = (211, 211, 211)
        replace_black = (255, 0, 0)
    elif option == "yellow":
        replace_white = (246, 255, 194)
        replace_black = (255, 215, 84)
    elif option == "red-black":
        replace_white = (255, 0, 0)
        replace_black = (0, 0, 0)
    else:
        replace_white = (255, 255, 255)
        replace_black = (0, 0, 0)

    for item in datas:
        # change all white (also shades of whites) pixels to yellow
        if item == (255, 255, 255):
            new_image_data.append(replace_white)
        elif item == (0, 0, 0):
            new_image_data.append((replace_black))
        else:
            new_image_data.append(item)

    # update image data
    img.putdata(new_image_data)

    return img


def encode_barcode():
    a = ImageWriter()
    with open("barcode.png", "wb") as f:
        EAN8(NUMBERS, writer=a).write(f)

    decodable = False
    height = 12
    while not decodable:
        # img = Image.open('barcode.png')
        img = change_color("barcode.png", COLOR)
        img = img.resize((160, 80))
        box = (30, 10, 130, height)
        img = img.crop(box)
        img2 = Image.open(INPUT_IMG)
        img2.paste(img, (0, img2.size[1] - img.size[1]))
        img2.save("output.jpg")
        if decode_barcode("output.jpg"):
            decodable = True
        height += 1

if __name__ == "__main__":
    encode_barcode()
