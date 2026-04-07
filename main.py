import numpy as np
import cv2 as cv

if __name__ == "__main__":
    img = cv.imread('earth.jpg')

    # turn darker pixels into white
    height, width, _ = img.shape
    for h in range(height):
        for w in range(width):
            pixel = img[h][w]
            if pixel[0] < 50 and pixel[1] < 50 and pixel[2] < 50:
                img[h][w] = (255, 255, 255)

    cv.imwrite("img/earth3.jpg", img)
