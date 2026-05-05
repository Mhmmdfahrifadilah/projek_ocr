import pytesseract, cv2

pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_image(image_path):
    img = cv2.imread(image_path)

    #cv2.imshow("weakltd", img)

    text = pytesseract.image_to_string(img)
    return text
    
    

hasil = ocr_image("img/lrm.jpg")
print(hasil)