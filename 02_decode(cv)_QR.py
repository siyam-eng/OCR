import cv2 as cv
from pyzbar.pyzbar import decode
from PIL import Image
def decode_QR(img_path):
    img = cv.imread(img_path)
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(img)
    return retval


# print(decode_QR('output.jpg'))

def decode_QR(img_path):
    img = Image.open(img_path)
    result = decode(img)
    for i in result:
        print(i.data.decode('utf-8'))



