import cv2
import math
cap = cv2.VideoCapture('movie.Mjpeg')
framerate = math.floor(cap.get(cv2.CAP_PROP_FPS))
length = math.floor(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print ("fr: {fr}\nlength: {length}".format(**{
    'fr': framerate,
    'length': length
}))
