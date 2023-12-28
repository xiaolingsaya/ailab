from serial.tools import list_ports
import pydobot
from picamera2 import Picamera2
import cv2
import numpy as np
import time

def painting():
    available_ports = list_ports.comports()
    print(f'available ports: {[x.device for x in available_ports]}')
    port = available_ports[0].device
    device = pydobot.Dobot(port=port, verbose=True)
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
    x0=-60
    y0=160
    z0=z
    edges=cv2.imread('/home/student/2100012869/finale/output.png')
    edges=255-edges
    edges= cv2.Canny(edges,50,150)
    # 找到轮廓并提取路径点
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours (edges, contours, -1, (0 ,255 ,0) , 1)
    cv2.imshow('image',edges)
    print("***********************************************start drawing!***********************************************")
    # 对每个轮廓进行处理
    i=0
    z += 30
    for contour in contours:
        # 逐点移动机器人
        i+=1
        # 下一个轮廓开始时放下（减少z）
        device.move_to(x+x0, y+y0, z, r, wait=True)
        for point in contour:
            z = z0
            y, x = point[0]
            print (x+x0,y+y0,z,r)
            # 假设这里设定机器人的移动参数
            device.move_to(x+x0, y+y0, z, r, wait=True)  # 移动到轮廓上的点
            
        # 当一个轮廓结束时，抬起（增加z）
        z += 30
        device.move_to(x+x0, y+y0, z, r, wait=True)
        device.wait(50)  # 等待一段时间
        
    # 结束后清理
    print(i)
    device.move_to(x0, y0, z+30, r, wait=True)  # 移动到结束点
    device.wait(500)  # 等待一段时间
    print("***********************************************finished!***********************************************")
    device.close()

painting()