import cv2


img = cv2.imread("shadow.png")

edges = cv2.Canny(img,100,200)
edges2 = cv2.Canny(img,10,100)
edges3 = cv2.Canny(img,150,175)
edges4 = cv2.Canny(img,100,200)

cv2.imshow("shadow", img)
cv2.imshow("shadow-borda", edges)
cv2.imshow("shadow-borda-2", edges2)
cv2.imshow("shadow-borda-3", edges3)
cv2.imshow("shadow-borda-4", edges4)
cv2.waitKey(0)
