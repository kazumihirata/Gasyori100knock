import cv2
import numpy as np

img = cv2.imread("../imori.jpg")

# bgr
blue = img[:, :, 0].copy()
green = img[:, :, 1].copy()
red = img[:, :, 2].copy()

# Y = 0.2126 R + 0.7152 G + 0.0722 B
out = 0.0722 * blue + 0.7152 * green + 0.2126 * red
# print(out)
# cast
out = out.astype(np.uint8)
# print(out)

cv2.imwrite('q2.jpg', out)
cv2.imshow('q2.jpg', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
