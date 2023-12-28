from picamera2 import Picamera2
import cv2
import numpy as np
import time
import sketch
import binary
from serial.tools import list_ports
import pydobot
import path

def lining():
    camera = Picamera2()
    camera.still_configuration.main.size = (160,120)
    camera.still_configuration.main.format = 'RGB888'
    camera.configure("still")
    camera.start ()
    time.sleep(1)
    def back(x):
        pass
    cv2.namedWindow('Output',256)
    cv2.createTrackbar('shadow','Output' ,0,255, back)
    cv2.createTrackbar('ksize','Output' ,0,250, back)
    print("press s to save the image and q to quit")
    print("you can still press s to save a new image than saved one")
    while(True):
        input_img = camera.capture_array("main")
        cv2.imshow('ori',input_img)
        gray_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
        inv_gray_img = 255 - gray_img
        ksize=ksize=int(cv2.getTrackbarPos('ksize','Output')/5)
        if ksize%2==0:
            ksize+=1
        sigma=0
        blur_img = cv2.GaussianBlur(inv_gray_img, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)
        sketch_img = cv2.divide(gray_img, 255 - blur_img, scale=256)  
        blurfinale = cv2.GaussianBlur(sketch_img, ksize=(7, 7), sigmaX=sigma, sigmaY=sigma)
        ret,binary = cv2.threshold(blurfinale,235,255,cv2.THRESH_BINARY)
        cv2.imshow('finale',binary)
        # 使用Canny边缘检测提取边缘
        edges = cv2.Canny(binary, 50, 150)
        inv_edges = 255 - edges
        cv2.imshow('Edges', inv_edges)
        inputkey=cv2.waitKey(1)
        if inputkey== ord('s'):
            cv2.imwrite('/home/student/2100012869/finale/output.png',inv_edges)
            finale=cv2.imread('/home/student/2100012869/finale/output.png')
            cv2.imshow('result',finale)
        if inputkey== ord('q'):
            path.painting()
            break
    camera.stop()
    cv2.destroyAllWindows()

def binary():
    camera = Picamera2()
    camera.still_configuration .main.size = (160,120)
    camera.still_configuration .main.format = 'RGB888'
    camera.configure("still")
    camera.start ()
    time.sleep(1)
    def back(x):
        pass
    cv2.namedWindow('Output',256)
    cv2.createTrackbar('shadow','Output' ,0,255, back)
    cv2.createTrackbar('ksize','Output' ,0,250, back)
    print("press s to save the image and q to quit")
    print("you can still press s to save a new image than saved one")
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
        inputkey=cv2.waitKey(1)
        if inputkey== ord('s'):
            cv2.imwrite('/home/student/2100012869/finale/output.png',inv_edges)
            finale=cv2.imread('/home/student/2100012869/finale/output.png')
            cv2.imshow('result',finale)
        if inputkey== ord('q'):
            path.painting()
            break
    camera.stop()
    cv2.destroyAllWindows()

print("welcome to drawing station!")
print("please choose the style you want:")
print("1 for the lining,2 for the binary")
print("you can check the sample to clarify your need")
inputchoice=cv2.waitKey(1)
if inputchoice== ord('1'):
    lining()
if inputchoice== ord('2'):
    binary()


