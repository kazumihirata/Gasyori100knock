import cv2

img = cv2.imread("../imori.jpg")

# bgr
blue = img[:, :, 0].copy()
green = img[:, :, 1].copy()
red = img[:, :, 2].copy()

# rgb
img[:, :, 0] = red
img[:, :, 1] = green
img[:, :, 2] = blue

cv2.imwrite('q1.jpg', img)
cv2.imshow('q1.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
