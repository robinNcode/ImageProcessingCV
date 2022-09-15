import numpy
import cv2
import math

img = cv2.imread('currenmenswatch1.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Inputed Image', img)
cv2.waitKey() # most important 

#print(img.min())
#print(img.max())

for xAxis in range(img.shape[0]):
    for yAxis in range(img.shape[0]):
        eachPixel = img.item(xAxis, yAxis)

        if eachPixel > 155:
            img.itemset((xAxis, yAxis), 200)
        else:
            img.itemset((xAxis, yAxis), 5)

cv2.imshow('Processed Image', img)
cv2.waitKey() # most important 

