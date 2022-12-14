import cv2
import math
from google.colab.patches import cv2_imshow

inputImage = cv2.imread('/content/kath_golap2.jpg', 1)

cv2_imshow(inputImage)

# Negate the original image
img_neg = 1 - inputImage

cv2_imshow(img_neg)

cv2.waitKey(0)
cv2.destroyAllWindows()