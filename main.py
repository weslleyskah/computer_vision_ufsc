import numpy as np
import cv2 as cv
import random

if __name__ == "__main__":
    
    img = cv.imread("img/space.jpg")

    img2 = cv.imread("img/creation.jpg")

    height, width, channels = img.shape

    img2 = cv.resize(img2, (width, height)) # resize the second img to match the first img

    for h in range(height):
        for w in range(width):
            pixel = img[h,w]
            if pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30:
                img[h,w] = img2[h,w]
                # Put the pixel of the second image in the first image if the pixel of the first image is 
                # darker than a certain threshold (30 for each channel)
    
    cv.imwrite("img/space_creation.jpg", img)
                



    