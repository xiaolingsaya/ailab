from picamera2 import Picamera2
import cv2
import numpy as np
import time
import sketch
import binary

print("welcome to drawing station!")
print("please choose the style you want:")
print("1 for the lining,2 for the binary")
print("you can check the sample to clarify your need")
if cv2.waitKey(1)==ord('1'):
    sketch.lining
if cv2.waitKey(1)==ord('2'):
    binary.binarydrawing