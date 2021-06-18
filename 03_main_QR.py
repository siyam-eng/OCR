import qrcode
from PIL import Image
import cv2 as cv


def encode_QR(text, image):
    img = qrcode.make(text)

    # pasting the QR code into another image
    inp_image = Image.open(image)
    qr_code_len = inp_image.size[1] * 0.12
    qr_code_len = 130 if qr_code_len < 130 else qr_code_len
    # print(qr_code_len)
    img.thumbnail((qr_code_len, qr_code_len))
    pos = (inp_image.size[0] - img.size[0], inp_image.size[1] - img.size[1])
    inp_image.paste(img, pos)
    inp_image.save("output.jpg")


def decode_QR(img_path):
    im = cv.imread(img_path)
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)
    return retval

if __name__ == '__main__':
    TEXT = "This is a sample text for QR code"
    IMAGE_PATH =  "input.jpg"
    encode_QR(TEXT, IMAGE_PATH)
    print(decode_QR('output.jpg'))
