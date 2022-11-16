import cv2
import numpy as np

def empty(a):
    pass


cv2.namedWindow("Ajuste")
cv2.resizeWindow("Ajuste",680,240)
cv2.createTrackbar("Hue Min","Ajuste",0,179,empty)
cv2.createTrackbar("Hue Max","Ajuste",179,179,empty)
cv2.createTrackbar("Sat Min","Ajuste",0,255,empty)
cv2.createTrackbar("Sat Max","Ajuste",255,255,empty)
cv2.createTrackbar("Val Min","Ajuste",0,255,empty)
cv2.createTrackbar("Val Max","Ajuste",255,255,empty)

while True:
    img = cv2.imread("shapes.png")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Ajuste")
    h_max = cv2.getTrackbarPos("Hue Max", "Ajuste")
    s_min = cv2.getTrackbarPos("Sat Min", "Ajuste")
    s_max = cv2.getTrackbarPos("Sat Max", "Ajuste")
    v_min = cv2.getTrackbarPos("Val Min", "Ajuste")
    v_max = cv2.getTrackbarPos("Val Max", "Ajuste")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Shadow",img)
    # cv2.imshow("Sombra",imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)