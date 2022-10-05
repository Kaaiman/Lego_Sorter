import cv2

def convert(border_percentage):
    imageLocation = 'photo.jpg'
    exportLocation = '/home/legopi/Lego_Sorter/Raspberry Pi/Output/output.jpg'

    img = cv2.imread(imageLocation)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
    edged = cv2.Canny(gray, 0, 255)  
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

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

    offsetPercentage = border_percentage

    xOffset = round((xM - x) * offsetPercentage)
    yOffset = round((yM - y) * offsetPercentage)

    x = x - xOffset
    y = y - yOffset
    xM = xM + xOffset
    yM = yM + yOffset

    img_crop = img_withrectangle[y:yM, x:xM]

    #save image
    cv2.imwrite(exportLocation,img_crop)
    