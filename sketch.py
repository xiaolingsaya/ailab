from picamera2 import Picamera2
import cv2
import numpy as np
import time
camera = Picamera2()
camera.still_configuration .main.size = (640,480)
camera.still_configuration .main.format = 'RGB888'
camera.configure("still")
camera.start ()
time.sleep(1)
while(True):
    input_img = camera.capture_array("main")
    cv2.imshow('ori',input_img)
    gray_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray_img)
    inv_gray_img = 255 - gray_img
    cv2.imshow('inv',inv_gray_img)
    ksize=21
    sigma=0
    blur_img = cv2.GaussianBlur(inv_gray_img, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)
    cv2.imshow('blur',blur_img)
    sketch_img = cv2.divide(gray_img, 255 - blur_img, scale=256)  
    cv2.imshow('middle',sketch_img)
    blurfinale = cv2.GaussianBlur(sketch_img, ksize=(7, 7), sigmaX=sigma, sigmaY=sigma)
    cv2.imshow('blurfinale',blurfinale)
    ret,binary = cv2.threshold(blurfinale,235,255,cv2.THRESH_BINARY)
    cv2.imshow('finale',binary)
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('/home/student/2100012869/finale/output.png',binary)
    if cv2.waitKey(1) == ord('q'):
        break
camera.stop()
cv2.destroyAllWindows()

