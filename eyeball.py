import rospy
import cv2
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from gaze_tracking import GazeTracking
from cv_bridge import CvBridge, CvBridgeError
gaze = GazeTracking()
class Zed_Video:
    def __init__(self):
        # subscribing to the image data from the virat camera
        self.image_sub = rospy.Subscriber(
            "zed2/zed_node/rgb/image_raw", Image, self.callback
        )
    def callback(self, data):

        bridge = CvBridge()

        try:
            # using CVbridge to convert a ros image to a cv2 image
            cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
            
            while True:
                _, frame = cv_image
                gaze.refresh()

        except CvBridgeError as e:
            rospy.logerr(e)

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
Zed_Video()
