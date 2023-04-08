import cv2
from gaze_tracking import GazeTracking


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
	_, frame = webcam.read()
	gaze.refresh()
	
 
