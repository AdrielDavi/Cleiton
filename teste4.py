import cv2
import math

img = cv2.imread('ex4.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, math.pi/180, 200)

angle = lines[0][0][1] * 180 / math.pi

# verificar a orientação da letra na imagem
rect = cv2.minAreaRect(cv2.findNonZero(edges))
if rect[1][0] > rect[1][1]:
    angle -= 90

rows, cols, _ = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 600, 600)
cv2.namedWindow('Aligned', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Aligned', 600, 600)

cv2.imshow('Original', img)
cv2.imshow('Aligned', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
