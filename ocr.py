import pytesseract, cv2

pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_image(image_path):
    img = cv2.imread(image_path)

    #ini buat menampilan gambar weakltd.jpg yang saya buat 
    cv2.imshow("weakltd", img)
    cv2.waitKey(0) #ini buat menahan jendela nya agar tidak langsung tertutup
    
    #ini buat menyimpan data text yang ada di lrm.jpg
    text = pytesseract.image_to_string(img)
    return text
    
    
hasil = ocr_image("img/lrm.jpg")
print(hasil)
