import cv2
import numpy as np

img = cv2.imread("../imori.jpg")

# bgr
blue = img[:, :, 0].copy()
green = img[:, :, 1].copy()
red = img[:, :, 2].copy()

# Y = 0.2126 R + 0.7152 G + 0.0722 B
out = 0.0722 * blue + 0.7152 * green + 0.2126 * red
out = out.astype(np.uint8)

# Binarization
print(out)
th = 128
out[out < th] = 0
out[out >= th] = 255

cv2.imwrite('q3.jpg', out)
cv2.imshow('q3.jpg', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
