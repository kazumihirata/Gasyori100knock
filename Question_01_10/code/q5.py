import cv2
import numpy as np

img = cv2.imread("../imori.jpg")
H, W, C = img.shape

# bgr
blue = img[:, :, 0].copy()
green = img[:, :, 1].copy()
red = img[:, :, 2].copy()

# Y = 0.2126 R + 0.7152 G + 0.0722 B
out = 0.0722 * blue + 0.7152 * green + 0.2126 * red
out = out.astype(np.uint8)

# Determine threshold of Otsu binarization
max_sigma = 0
max_t = 0

for i in range(1, 255):
    v0 = out[np.where(out < i)]
    m0 = np.mean(v0) if len(v0) > 0 else 0.
    w0 = len(v0) / (H * W)
    v1 = out[np.where(out >= i)]
    m1 = np.mean(v1) if len(v1) > 0 else 0.
    w1 = len(v1) / (H * W)
    sigma = w0 * w1 * ((m0 - m1) ** 2)
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = i

# Binarization
print("threshhold >>", max_t)
th = max_t
out[out < th] = 0
out[out >= th] = 255

cv2.imwrite('q5.jpg', out)
cv2.imshow('q5.jpg', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
