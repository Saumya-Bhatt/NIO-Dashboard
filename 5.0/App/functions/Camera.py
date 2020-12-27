import urllib, urllib.request
import cv2
import numpy as np

#url = 'http://192.168.43.175:8080/shot.jpg'

def stream_video(url_inp):

    url = 'http://' + url_inp + '/shot.jpg'
    while True:
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        cv2.imshow('test',img)
        if ord('q')==cv2.waitKey(10):
            exit(0)
    return None