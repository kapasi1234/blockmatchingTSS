import framecollect
import cv2

import numpy as np

from PIL import Image, ImageDraw

videopath = 'casa_360.mp4'

framecollect.getFrames(videopath, 0, 100)

