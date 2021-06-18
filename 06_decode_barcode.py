from pyzbar.pyzbar import decode
from PIL import Image


def decode_barcode(img_path):
    img = Image.open(img_path)
    result = decode(img)
    for i in result:
        print(i.data.decode("utf-8"))


IMAGE_PATH = "output.jpg"
decode_barcode(IMAGE_PATH)
