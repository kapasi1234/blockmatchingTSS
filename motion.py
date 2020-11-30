from cv2 import cv2
import numpy as np
import os
import pathlib
path ="C:\\Users\\rvalentin\\Desktop\\vectors.bin"


vectorsFile = open(path,"r+")
buffer = np.fromfile(vectorsFile,dtype=np.int_)
vectors = []

for i in range(0,len(buffer),2):
    vectors.append((buffer[i:i+2]))
yuv_filename = "D:\Visual Studio Code\DMV\captureYUV422P.yuv"
#flow=[]
vectorsFile.close()


width,height= 1280, 720

file_size = os.stat(yuv_filename).st_size
n_frames = file_size // (width*height*2)
prevFrame = None
f = open(yuv_filename, 'rb')
yuv = np.frombuffer(f.read(width*height*2), dtype=np.uint8).reshape(height,width,2)
prevFrame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_YUYV)
yuv =np.frombuffer(f.read(width*height*2), dtype=np.uint8).reshape(height,width,2)
frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_YUYV)

f.close()

bcount = 0
blockSize = 8 
for y in range(0, int(90*8), 8):
        for x in range(0, int(160*8), 8):
            if (x,y) != (vectors[bcount][0],vectors[bcount][1]) :
                
                p= vectors[bcount]
                cv2.arrowedLine(frame,(p[0]+int(blockSize/2),p[1]+int(blockSize/2)),(x+int(blockSize/2),y+int(blockSize/2)), (0,255,0), 1)
            bcount = bcount + 1
cv2.imshow("Vektori",frame)
cv2.waitKey()
# Convert YUV420 to Grayscale
#old_gray = cv2.cvtColor(old_yuv, cv2.COLOR_YUV2GRAY_I420)
#cv2.imshow('frame_gs',old_gray)
#cv2.waitKey()
