import cv2


# img = cv2.imread("shadow.png")

# cv2.imshow("shadow", img)

# cv2.waitKey(2000)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    sucess,img = cap.read()
    cv2.imshow("webcam",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
