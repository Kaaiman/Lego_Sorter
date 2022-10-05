import extcolors

def rgbToName(pulled):
    blackR = 5
    blackG = 19
    blackB = 29

    whiteR = 177
    whiteG = 140
    whiteB = 147
    
    backR = 188
    backG = 171
    backB = 182
    
    redR = 153
    redG = 26
    redB = 9

    greenR = 105
    greenG = 160
    greenB = 25

    blueR = 0
    blueG = 79
    blueB = 113

    brownR = 50
    brownG = 42
    brownB = 37

    greyR = 164
    greyG = 149
    greyB = 157

    yellowR = 227
    yellowG = 157
    yellowB = 11

    tanR = 158
    tanG = 141
    tanB = 108

    step1 = pulled.replace('[','')
    step2 = step1.replace(']', '')
    step3 = step2.replace(' ', '')
    step4 = step3.replace('(', '')
    step5 = step4.replace(')', '')

    R = ''
    B = ''
    G = ''
    i = 0
    while step5[i] != ',':
        R += step5[i]
        i += 1
    i += 1
    while step5[i] != ',':
        G += step5[i]
        i += 1
    i += 1
    while step5[i] != ',':
        B += step5[i]
        i += 1

    R = int(R)
    G = int(G)
    B = int(B)

    blackDiff = abs(R - blackR) + abs(G - blackG) + abs(B - blackB)
    whiteDiff = abs(R - whiteR) + abs(G - whiteG) + abs(B - whiteB)
    redDiff = abs(R - redR) + abs(G - redG) + abs(B - redB)
    greenDiff = abs(R - greenR) + abs(G - greenG) + abs(B - greenB)
    blueDiff = abs(R - blueR) + abs(G - blueG) + abs(B - blueB)
    brownDiff = abs(R - brownR) + abs(G - brownG) + abs(B - brownB)
    greyDiff = abs(R - greyR) + abs(G - greyG) + abs(B - greyB)
    yellowDiff = abs(R - yellowR) + abs(G - yellowG) + abs(B - yellowB)
    tanDiff = abs(R - tanR) + abs(G - tanG) + abs(B - tanB)
    backDiff = abs(R - backR) + abs(G - backG) + abs(B - backB)

    diffs = [blackDiff, whiteDiff, redDiff, greenDiff, blueDiff, brownDiff, greyDiff, yellowDiff, tanDiff, backDiff]
    diffs.sort()
    minDiff = diffs[0]

    if minDiff == backDiff:
        color ='back'
    elif minDiff == whiteDiff:
        color = 'white'
    elif minDiff == blackDiff:
        color = 'black'
    elif minDiff == redDiff:
        color = 'red'
    elif minDiff == greenDiff:
        color = 'green'
    elif minDiff == blueDiff:
        color = 'blue'
    elif minDiff == brownDiff:
        color = 'brown'
    elif minDiff == greyDiff:
        color = 'grey'
    elif minDiff == yellowDiff:
        color = 'yellow'
    else:
        color = 'tan'
    return color

def photo_to_color():
    pulledList = extcolors.extract_from_path('output.jpg', tolerance = 5, limit = 10)

    rgbList = pulledList[0]

    print(pulledList)

    rgb = str(rgbList[0])

    color = rgbToName(rgb)

    i = 1

    while color == 'back':
        rgb = str(rgbList[i])
        color = rgbToName(rgb)
        i = i + 1

    print(i)
    return color
