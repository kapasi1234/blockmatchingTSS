import cv2
import numpy as np

import sys

#______________________________________________________________________

class YUV422_Loader():

    def __init__(self, frame_width, frame_height):

        self.frame_width   = frame_width
        self.frame_height  = frame_height
        
    def grab_uyvy_frame(self, frame_raw):
                
        Y1  = frame_raw[0::4]
        U = frame_raw[1::4]
        Y2  = frame_raw[2::4]
        V = frame_raw[3::4]
        
        UV = np.empty((self.frame_height*self.frame_width), dtype=np.uint8)
        YY = np.empty((self.frame_height*self.frame_width), dtype=np.uint8)
        
        UV[0::2] = np.fromstring(U,  dtype=np.uint8)
        UV[1::2] = np.fromstring(V,  dtype=np.uint8)
        YY[0::2] = np.fromstring(Y1, dtype=np.uint8)
        YY[1::2] = np.fromstring(Y2, dtype=np.uint8)
        
        UV = UV.reshape((self.frame_height, self.frame_width))
        YY = YY.reshape((self.frame_height, self.frame_width))
        
        frame_yuyv = cv2.merge([UV, YY])
        
        return frame_yuyv
#______________________________________________________________________
        
if __name__ == "__main__":
    
    if len(sys.argv) >= 3:
        width         = int(sys.argv[1])
        height        = int(sys.argv[2])
        bytes_to_ign  = 0
        scaling_fact  = 1.0
        
        if len(sys.argv) >= 4:
            bytes_to_ign = int(sys.argv[3])
            
        if len(sys.argv) == 5:
            scaling_fact = float(sys.argv[4])
        
        loader = YUV422_Loader(width, height)
        
        i = 0
        while True:
            frame_raw = sys.stdin.read((width * 2) * height)
            
            if frame_raw == '':
                break
                
            frame_uyvy = loader.grab_uyvy_frame(frame_raw)
            frame_bgr  = cv2.cvtColor(frame_uyvy, cv2.COLOR_YUV2BGR_YUYV)
            
            if scaling_fact != 1:
                frame_bgr = cv2.resize(frame_bgr, (int(frame_bgr.shape[1]*scaling_fact), int(frame_bgr.shape[0]*scaling_fact)))
            
            cv2.imshow("", frame_bgr)
            cv2.waitKey(1)
            
            print >> sys.stderr, i+1
            i += 1
            
            sys.stdin.read(bytes_to_ign)
        
    else:
        print ("program shows frames of YUV movie (read from stdin), in which each line is multiplexed 4:2:2 component video (Cb Y Cr Y...) format.")
        print ("")
        print ("Usage:   python -u", sys.argv[0], "WIDTH HEIGHT [NUM-IGNORE-LAST-BYTES] [DISPLAY-SCALE]")
        print ("           WIDTH  - width of a frame")
        print ("           HEIGHT - height of a frame")
        print ("           NUM-IGNORE-LAST-BYTES  - optional; number of bytes to in a movie stream (in case of concatenated video and audio raw, see bmdcapture), default: 0")
        print ("           DISPLAY-SCALE          - optional; scaling factor for displayed image; default: 1.0")
        print ("")
        print ("Example: cat movie.yuv | python -u", sys.argv[0], "720 576")
