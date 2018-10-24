# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 02:22:09 2018

@author: Mursil
"""

import cv2


first_frame=None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    gray_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame= cv2.GaussianBlur(gray_frame,(21,21), 0)
    
    
    if first_frame is None:
        first_frame=gray_frame
        continue
    
    delta_frame=cv2.absdiff(first_frame, gray_frame)
    
    delta_thresh=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    
    cv2.imshow("Gray Frame", gray_frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", delta_thresh)
    
    
    
    print (check)
    print(frame)
    print(delta_frame)
    
     
    key = cv2.waitKey(1)
    if key==ord('x'):
        break



video.release()
cv2.destroyAllWindows()