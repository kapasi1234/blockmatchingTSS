
import sys
import numpy as np
from cv2 import cv2 
import tss
import new_tss

import copy
import ebma
import framecollect as fc

videopath = "casa_360.mp4"
prevFrame= "testImages/frame91.png"
frame = "testImages/frame94.png"
#framecollect.getFrames(videopath)
#cv2.arrowedLine(image, start_point, end_point, color, thickness)
"""
cv2.imread(prevFrame)
editedFrame = new_tss.main(cv2.imread(prevFrame),cv2.imread(frame))
cv2.imshow(videopath,editedFrame)
cv2.waitKey()

"""



def run_TSSvideo(videopath):
    video = cv2.VideoCapture(videopath)
    
    
    prevFrame = None
    
    count=True
    while video.isOpened():
        
        ret, frame = video.read()
        
        if count:
            prevFrame = frame
            count = False
        
        editedFrame = new_tss.main(prevFrame,frame,blockSize=8)
        prevFrame = frame
        

        cv2.imshow(videopath,editedFrame)
        if cv2.waitKey(1) == ord('q'):
            break
        
  
    video.release()
    
    cv2.destroyAllWindows()

def run_EBMAvideo(videopath):
    video = cv2.VideoCapture(videopath)
    
    prevFrame = None
    count=True
    while video.isOpened():
        
        ret, frame = video.read()
        
        if count:
            prevFrame = frame
            count = False
        
        editedFrame = ebma.main(prevFrame,frame, blockSize=8)
        prevFrame = frame
       
        cv2.imshow(videopath,editedFrame)
        if cv2.waitKey(1) == ord('q'):
            break
        
    
    video.release()
    
    cv2.destroyAllWindows()
def run_TSS2frames(frame, prevFrame):
    
    editedFrame = new_tss.main(cv2.imread(prevFrame),cv2.imread(frame))
    cv2.imshow(videopath,editedFrame)
    cv2.waitKey()
def run_EBMA2frames(frame, prevFrame):
    
    editedFrame = ebma.main(cv2.imread(prevFrame),cv2.imread(frame))
    cv2.imshow(videopath,editedFrame)
    cv2.waitKey()

run_TSSvideo(videopath)
#run_EBMAvideo(videopath)
#run_EBMA2frames(frame,prevFrame)
#run_TSS2frames(frame,prevFrame)