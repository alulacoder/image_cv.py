import cv2

img = cv2.imread("open_cv/image/pikachu.jpeg")
img = cv2.resize(img, (0,0), fx=2, fy=2)

cv2. imwrite("pi.jpeg", img)
cv2.imshow("Pikachu Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()