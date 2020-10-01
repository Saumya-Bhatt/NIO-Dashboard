import cv2
import numpy as np

import PIL
from PIL import Image

#This variable we use to store the pixel location
refPt = []

def image_browser(imported_image):
    #click event function
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x,",",y)
            refPt.append([x,y])
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = str(x)+", "+str(y)
            cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 2)
            cv2.imshow("Select TOP-LEFT and BOTTOM-RIGHT points", img)

        if event == cv2.EVENT_RBUTTONDOWN:
            blue = img[y, x, 0]
            green = img[y, x, 1]
            red = img[y, x, 2]
            font = cv2.FONT_HERSHEY_SIMPLEX
            strBGR = str(blue)+", "+str(green)+","+str(red)
            cv2.putText(img, strBGR, (x,y), font, 0.5, (0,255,255), 2)
            cv2.imshow("Select TOP-LEFT and BOTTOM-RIGHT points", img)



    #Here, you need to change the image name and it's path according to your directory
    img = cv2.imread(imported_image)
    cv2.namedWindow('Select TOP-LEFT and BOTTOM-RIGHT points',cv2.WINDOW_NORMAL)
    height,width = img.shape[:2]
    cv2.resizeWindow('Select TOP-LEFT and BOTTOM-RIGHT points',width//2,height//2)
    cv2.imshow("Select TOP-LEFT and BOTTOM-RIGHT points", img)

    #calling the mouse click event
    cv2.setMouseCallback("Select TOP-LEFT and BOTTOM-RIGHT points", click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imgp = Image.open(imported_image)

    imgp_crop = imgp.crop((refPt[0][0],refPt[0][1],refPt[1][0],refPt[1][1]))
    #imgp_crop = imgp_crop.convert('L')
    imgp_crop.save('crop.png',type='PNG')

    return None