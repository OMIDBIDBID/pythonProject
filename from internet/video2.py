import cv2
import numpy as np
cap=cv2.VideoCapture(0)
      while (True):
           ret,frame=cap.read()
            cv2.line(frame,(100,200),(200,600),(11,8,255),5)
             cv2.rectangle(frame,(100,200),(200,300),(0,0,255),5)
               cv2.imshow('webcam',frame)
    if cv2.waitKey(1)&0xFF== ord('q'):
        break
        cap.release()
        cv2.destroyAllwindows()
