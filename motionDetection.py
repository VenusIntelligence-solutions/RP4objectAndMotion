import cv2
from picamera2 import Picamera2

picam2 = Picamera2()

picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

while True:
    frame1 = picam2.capture_array()
    frame2 = picam2.capture_array()

    motiondiff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh,result = cv2.threshold(blur,15,255,cv2.THRESH_BINARY)
    dilation = cv2.dilate(result,None,iterations=3)
    contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    cv2.imshow ("OUTPUTJA" , frame1)
    
    frame1 = frame2

