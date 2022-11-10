import cv2
import math
img = cv2.imread('../images/currenmenswatch1.png', cv2.IMREAD_GRAYSCALE)
brightImage = img.copy()
darkImage = img.copy()

c = 200 # positive constant

cv2.imshow('input image',img)

for xAxis in range(img.shape[0]):
    for yAxis in range(img.shape[1]):
        eachPixel = img.item(xAxis, yAxis) # S

        gamma_one = (c*(eachPixel/c) ** 0.4)
        gamma_two = (c*(eachPixel/c) ** 2.2)

        brightImage.itemset((xAxis, yAxis), gamma_one)
        darkImage.itemset((xAxis, yAxis), gamma_two)

#cv2.imshow('gamma bright image', brightImage)
#cv2.imshow('gamma dark image', darkImage)

im_h = cv2.hconcat([brightImage, darkImage])
cv2.imshow('data/dst/opencv_hconcat.jpg', im_h)

cv2.waitKey(0)
cv2.destroyAllWindows()