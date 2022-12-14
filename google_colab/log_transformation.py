import cv2
import math
from google.colab.patches import cv2_imshow

# Read an image
inputImage = cv2.imread('../images/kath_golap.jpeg', cv2.IMREAD_UNCHANGED)
out = inputImage.copy()
c = 31
cv2_imshow(inputImage)

for xAxis in range(inputImage.shape[0]):
    for yAxis in range(inputImage.shape[1]):
        eachPixel = inputImage.item(xAxis, yAxis)
        
        d = math.pow(eachPixel / c, 2)
        r = d - 1
        out.itemset((xAxis, yAxis), r)
        
cv2_imshow(out)

cv2.waitKey(0)
cv2.destroyAllWindows()
