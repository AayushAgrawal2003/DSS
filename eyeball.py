import rospy
import cv2
from sensor_msgs.msg import Image
from gaze_tracking import GazeTracking
from cv_bridge import CvBridge, CvBridgeError

rospy.init_node('zed_converter',anonymous=True)
gaze = GazeTracking()
class Zed_Video:
    def __init__(self):
        # subscribing to the image data from the virat camera
        self.image_sub = rospy.Subscriber(
            "zed2i/zed_node/rgb_raw/image_raw_color", Image, self.callback
        )
        self.bridge = CvBridge()
        
    def callback(self, data):

        try:
            # using CVbridge to convert a ros image to a cv2 image
            cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
            
            while True:
                _, frame = cv_image
                gaze.refresh()

        except CvBridgeError as e:
            rospy.logerr(e)
            
vd=Zed_Video()
rospy.spin()
