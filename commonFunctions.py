import cv2
import numpy as np


def common_functions():
    img = cv2.imread("Resources/lena.png")
    kernel = np.ones((5, 5), np.uint8)

    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
    imgCanny = cv2.Canny(img, 250, 100)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
    imgErode = cv2.erode(imgDilation, kernel, iterations=1)

    cv2.imshow("grey Image", imgGrey)
    cv2.imshow("Blur Image", imgBlur)
    cv2.imshow("Canny Image", imgCanny)
    cv2.imshow("Dilated Image", imgDilation)
    cv2.imshow("Eroded Image", imgErode)
    cv2.waitKey(0)
