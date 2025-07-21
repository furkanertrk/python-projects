import cv2

resim = cv2.imread('resim1.jpeg')
gri_resim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
cv2.imwrite('resim1_gri.jpeg',gri_resim)

cv2.imshow("Orijinal Resim", resim)
cv2.imshow("Gri Tonlamali Resim", gri_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()