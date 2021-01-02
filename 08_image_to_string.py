from PIL import Image, ImageOps
import pytesseract


pytesseract.pytesseract.tesseract_cmd = (
    "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)


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
        replace_white = (0, 0, 0)
        replace_black = (255, 255, 255)

    for item in datas:
        # change all white (also shades of whites) pixels to yellow
        if not (item[0] > 210 and item[1] > 210 and item[2] > 210):
            new_image_data.append(replace_white)
        else:
            new_image_data.append(item)

    # update image data
    img.putdata(new_image_data)

    return img


img = change_color("image.png")
img.show()
print(img.size)

text = pytesseract.image_to_string(img)
print(text.strip())
