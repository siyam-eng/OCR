from pyzbar.pyzbar import decode
from PIL import Image

def decode_QR(img_path):
    img = Image.open(img_path)
    result = decode(img)
    for i in result:
        print(i.data.decode('utf-8'))
