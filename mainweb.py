import cv2
import pytesseract as pt
import pyttsx3
import pyautogui
from spellchecker import SpellChecker

spell = SpellChecker(language='pt') #Dicionário português - Portugal
engine = pyttsx3.init()
pt.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe")
config = r'--oem 2 --psm 6'            # OK:  r'--oem 2 --psm 6'

video = cv2.VideoCapture(0)


while True:
    check, img = video.read()
    cv2.imshow("img", img)
    cv2.imwrite("capture.png", img)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break

imagem = cv2.imread("capture.png")
frase = pt.pytesseract.image_to_string(imagem, lang= "por")
#words: list = frase.split()
#list_of_correct_words = [spell.correction(word) for word in words if spell.correction(word) is not None]
#string_sem_loop = ' '.join(list_of_correct_words)
#print (string_sem_loop)

print(frase)

caixas = (pt.pytesseract.image_to_boxes(imagem))
imH,imW,_ = imagem.shape

for b in caixas.splitlines():
    b = b.split(' ')
    letra,x,y,w,h = b[0],int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(imagem,(x,imH-y),(w,imH-h),(0,0,255),1)

cv2.imshow("resultado",imagem)
cv2.waitKey(0)
