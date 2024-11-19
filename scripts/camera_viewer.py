from cv_bridge import CvBridge
import cv2

bridge = CvBridge()
cv_image = bridge.imgmsg_to_cv2(image)

