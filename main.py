# Created by Ahmadreza Anaami
import cv2 ;


img = cv2.imread("RES/1.jpg", 1 )
size = (900 ,700)
img = cv2.resize(img  , size)
rect = []
roi = cv2.selectROI("cropped pic" , img , False)
croped_img = img[ int(roi[1]):int(roi[1]+roi[3]) , int(roi[0]) : int(roi[0] + roi[2]) ]
croped_img = cv2.resize( croped_img , size)
cv2.imshow("cropped" , croped_img)
cv2.waitKey()
cv2.destroyAllWindows();