import os
import cv2
import numpy as np

def white_convert(border_percentage, noise_thresh):
    input_dir = 'photo.jpg'
    output_dir = '/home/legopi/Lego_Sorter/Raspberry Pi/Output/output.jpg'

    bgr_input = cv2.imread(input_dir)
    hsv_input = cv2.cvtColor(bgr_input, cv2.COLOR_BGR2HSV)

    white_mask = cv2.inRange(hsv_input, np.array([0, 0, 0]), np.array([30, 255, 255]))

    cv2.imshow('mask', white_mask)
    cv2.waitKey(0)

    shadow_mask = cv2.inRange(bgr_input, np.array([100, 100, 100]), np.array([160, 160, 160]))

    cv2.imshow('mask', shadow_mask)
    cv2.waitKey(0)

    final_mask = cv2.max(white_mask, shadow_mask)

    cv2.imshow('mask', final_mask)
    cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(final_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_img = bgr_input.copy()

    cv2.drawContours(contour_img, contours, -1, (0,255,0), 3)

    cv2.imshow('contours', contour_img)
    cv2.waitKey(0)

    xList = []
    yList = []
    wList = []
    hList = []


    for i in contours:
        x,y,w,h = cv2.boundingRect(i)
        if w * h > noise_thresh: 
            xList.append(x)
            yList.append(y)
            wList.append(w)
            hList.append(h)

    xListMax = []
    yListMax = []

    xLength = len(xList) - 1
    yLength = len(yList) - 1

    i = 0
    while i <= xLength:
        newX = xList[i] + wList[i]
        xListMax.append(newX)
        i = i + 1
    i = 0
    while i <= yLength:
        newY = yList[i] + hList[i]
        yListMax.append(newY)
        i = i + 1
        
    xList.sort()
    yList.sort()
    xListMax.sort()
    yListMax.sort()

    x = xList[0]
    y = yList[0]
    xM = xListMax[-1]
    yM = yListMax[-1]

    offsetPercentage = border_percentage

    xOffset = round((xM - x) * offsetPercentage)
    yOffset = round((yM - y) * offsetPercentage)

    x = x - xOffset
    y = y - yOffset
    xM = xM + xOffset
    yM = yM + yOffset

    img_crop = bgr_input[y:yM, x:xM]

    cv2.imshow('cropped', img_crop)
    cv2.waitKey(0)

    cv2.imwrite(output_dir, img_crop)
