import numpy as np
import cv2
import math
from google.colab.patches import cv2_imshow

img = cv2.imread('../images/currenmenswatch1.png', cv2.IMREAD_GRAYSCALE)
out=img.copy()
c = 31

cv2_imshow(img)

for xAxis in range(img.shape[0]):
    for yAxis in range(img.shape[1]):
        eachPixel = img.item(xAxis, yAxis)
        d = math.pow(eachPixel / c, 2)
        r = d - 1
        out.itemset((xAxis, yAxis), r)
        
cv2_imshow(out)

cv2.waitKey(0)
cv2.destroyAllWindows()