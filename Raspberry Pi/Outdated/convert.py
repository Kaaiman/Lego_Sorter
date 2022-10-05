import cv2
import numpy as np
import os

def convert1():
    imageLocation = 'photo.jpg'
    backgroundLocation = 'background.jpg'
    exportLocation = 'output.jpg'

    img = cv2.imread(imageLocation, cv2.IMREAD_UNCHANGED)
    bg = cv2.imread(backgroundLocation, cv2.IMREAD_UNCHANGED)
    #convert img to grey
    img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_bg_grey = cv2.cvtColor(bg,cv2.COLOR_BGR2GRAY)

    #img_step = cv2.absdiff(img_bg_grey,img_grey)

    #set a thresh higher is less lower is more
    thresh = 5
    #get threshold image
    ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
    #find contours
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #create an empty image for contours
    img_withrectangle = img.copy()
    # draw the contours on the empty image

    xList = []
    yList = []
    wList = []
    hList = []


    for i in contours:
        x,y,w,h = cv2.boundingRect(i)
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

    offsetPercentage = 0.1
    xOffset = round((xM - x) * offsetPercentage)
    yOffset = round((yM - y) * offsetPercentage)

    x = x - xOffset
    y = y - yOffset
    xM = xM + xOffset
    yM = yM + yOffset

    img_crop = img_withrectangle[y:yM, x:xM]

    #save image
    cv2.imwrite(exportLocation,img_crop)

convert1()