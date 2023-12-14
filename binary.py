from picamera2 import Picamera2
import cv2
import numpy as np
import time
def binary():
    camera = Picamera2()
    camera.still_configuration .main.size = (640,480)
    camera.still_configuration .main.format = 'RGB888'
    camera.configure("still")
    camera.start ()
    time.sleep(1)
    def back(x):
        pass
    cv2.namedWindow('Output',256)
    cv2.createTrackbar('shadow','Output' ,0,255, back)
    cv2.createTrackbar('ksize','Output' ,0,250, back)
    while(True):
        input_img = camera.capture_array("main")
        cv2.imshow('ori',input_img)
        gray_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray',gray_img)
        ksize=int(cv2.getTrackbarPos('ksize','Output')/5)
        if ksize%2==0:
            ksize+=1
        sigma=0
        blurry = cv2.GaussianBlur(gray_img, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)
        shadow=cv2.getTrackbarPos('shadow','Output')
        ret,binary = cv2.threshold(blurry,shadow,255,cv2.THRESH_BINARY)
        cv2.imshow('finale',binary)
        edges = cv2.Canny(binary, 50, 150)
        inv_edges = 255 - edges
        cv2.imshow('Edges', inv_edges)
        if cv2.waitKey(1) == ord('s'):
            cv2.imwrite('/home/student/2100012869/finale/output.png',binary)
        if cv2.waitKey(1) == ord('q'):
            break
    camera.stop()
    cv2.destroyAllWindows()

