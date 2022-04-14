import cv2
import numpy as np

img = cv2.imread("gambar1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Original", img)
cv2.imshow("Gambar gambar1 Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()